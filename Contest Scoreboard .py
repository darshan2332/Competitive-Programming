def process_submissions(submissions):
    scoreboard = {}
    for submission in submissions:
        contestant, problem, time, status = submission.split()
        contestant = int(contestant)
        problem = int(problem)
        time = int(time)
        if status == 'C':
            if contestant not in scoreboard:
                scoreboard[contestant] = {'solved': 0, 'penalty': 0}
            scoreboard[contestant]['solved'] += 1
            scoreboard[contestant]['penalty'] += time
        elif status == 'I':
            if contestant not in scoreboard:
                scoreboard[contestant] = {'solved': 0, 'penalty': 0}
            scoreboard[contestant]['penalty'] += 20
    return scoreboard

def print_scoreboard(scoreboard):
    sorted_scoreboard = sorted(scoreboard.items(), key=lambda x: (-x[1]['solved'], x[0]))
    for contestant, stats in sorted_scoreboard:
        print(f"{contestant} {stats['solved']} {stats['penalty']}")

def case():
    cases = int(input())
    for _ in range(cases):
        submissions = []
        while True:
            line = input()
            if line:
                submissions.append(line)
            else:
                break
        scoreboard = process_submissions(submissions)
        print_scoreboard(scoreboard)
        print()
case()
