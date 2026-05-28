from flask import Flask, render_template, request

app = Flask(__name__)

DEFAULT_TASKS = [
    {"id": "T1", "time": 4.0, "predecesor": []},
    {"id": "T2", "time": 2.0, "predecesor": ["T1"]},
    {"id": "T3", "time": 5.0, "predecesor": ["T1"]},
    {"id": "T4", "time": 4.0, "predecesor": ["T2"]},
    {"id": "T5", "time": 3.0, "predecesor": ["T2"]},
    {"id": "T6", "time": 6.0, "predecesor": ["T3", "T4"]},
    {"id": "T7", "time": 2.0, "predecesor": ["T5"]},
    {"id": "T8", "time": 3.0, "predecesor": ["T6", "T7"]},
    {"id": "T9", "time": 2.0, "predecesor": ["T8"]},
    {"id": "T10", "time": 3.0, "predecesor": ["T9"]},
]


def parse_predecessors(value):
    if not value:
        return []
    return [item.strip().upper() for item in value.split(',') if item.strip()]


def compute_rpw(tasks):
    successors = {task["id"]: set() for task in tasks}
    for task in tasks:
        for pred in task["predecesor"]:
            if pred in successors:
                successors[pred].add(task["id"])

    memo = {}

    def rpw(task_id):
        if task_id in memo:
            return memo[task_id]
        weight = next(item["time"] for item in tasks if item["id"] == task_id)
        for nxt in successors[task_id]:
            weight += rpw(nxt)
        memo[task_id] = weight
        return weight

    ranked = []
    for task in tasks:
        ranked.append({
            "id": task["id"],
            "time": task["time"],
            "predecesor": task["predecesor"],
            "rpw": rpw(task["id"]),
        })

    ranked.sort(key=lambda item: (-item["rpw"], item["id"]))
    return ranked, successors


def assign_stations(tasks, cycle_time):
    ranked, _ = compute_rpw(tasks)
    stations = []
    assigned = set()

    for task in ranked:
        placed = False
        for station in stations:
            if station["used"] + task["time"] <= cycle_time and set(task["predecesor"]).issubset(assigned):
                station["tasks"].append(task)
                station["used"] += task["time"]
                assigned.add(task["id"])
                placed = True
                break

        if not placed:
            stations.append({"tasks": [task], "used": task["time"]})
            assigned.add(task["id"])

    total_time = sum(item["time"] for item in tasks)
    utilization = (total_time / (cycle_time * len(stations))) * 100 if stations else 0
    idle_time = sum(cycle_time - station["used"] for station in stations)

    return {
        "ranked": ranked,
        "stations": stations,
        "total_time": total_time,
        "utilization": utilization,
        "idle_time": idle_time,
    }


@app.route('/')
def home():
    return render_template('Balanceo.html', tasks=DEFAULT_TASKS, cycle_time=12.0)


@app.route('/Balanceo', methods=['GET', 'POST'])
def balanceo():
    tasks = list(DEFAULT_TASKS)
    cycle_time = 12.0

    if request.method == 'POST':
        cycle_time = float(request.form.get('cycle_time', 12.0) or 12.0)
        tasks = []
        for i in range(1, 11):
            time_value = request.form.get(f'task{i}_time', '').strip()
            if time_value == '':
                continue
            tasks.append({
                "id": f'T{i}',
                "time": float(time_value),
                "predecesor": parse_predecessors(request.form.get(f'task{i}_pred', '')),
            })

        if not tasks:
            tasks = list(DEFAULT_TASKS)

    result = assign_stations(tasks, cycle_time)
    return render_template('Balanceo.html', tasks=tasks, cycle_time=cycle_time, result=result)


if __name__ == '__main__':
    app.run(debug=True)