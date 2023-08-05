# def human_seconds(s):
#     MINUTE = 60
#     HOUR = MINUTE * 60
#     DAY = HOUR * 24
#     # s = int(s)
#     days = int(s / (60 * 60 * 24))
#     hours = int(s % (60 * 60 * 24)  / (60 * 60))
#     minutes = int(s % (60 * 60 * 24)  % (60 * 60) / 60 )
#     seconds = s % ()
#     # hours = int(s / HOUR)
#     print("HOURS", hours)
#     print("MINUTES", minutes)
#     print("SECONDS", seconds)
#     # days = int(hours / 24)
#     # print("DAYS", days)
#     # days = s / (60 * 60 * 24)
#     # print("DAYS", days)
#     # hours = s % (60 * 60 * 24)
#     parts = []
#
#     def pluralize(x):
#         return 's' if x > 1 else ''
#
#     if days:
#         parts.append('{} day{}'.format(days, pluralize(days)))
#
#     if hours:
#         parts.append('{} hour{}'.format(hours, pluralize(hours)))
#
#     if minutes and not days:
#         parts.append('{} minute{}'.format(minutes, pluralize(minutes)))
#
#     # while not parts:
#     #     if len(parts) >= 2:
#     #         break
#     # # if days:
#     #     return '{} days {} hours'.format(days, hours)
#     # minutes = hours % 60
#     # if hours:
#     #     return '{} hours {} minutes'.format(hours, minutes)
#     return ' '.join(parts)


def humanize_time(amount, units):
    intervals = (1, 60, 60 * 60, 60 * 60 * 24, 604800, 2419200, 29030400)
    names = (
        ("second", "seconds"),
        ("minute", "minutes"),
        ("hour", "hours"),
        ("day", "days"),
        ("week", "weeks"),
        ("month", "months"),
        ("year", "years"),
    )

    result = []
    unit = [x[1] for x in names].index(units)
    # Convert to seconds
    amount = amount * intervals[unit]
    for i in range(len(names) - 1, -1, -1):
        a = int(amount) // intervals[i]
        if a > 0:
            result.append((a, names[i][1 % a]))
            amount -= a * intervals[i]
    return result


def humanize_seconds(seconds):
    parts = ["{} {}".format(x, y) for x, y in humanize_time(seconds, "seconds")]
    return " ".join(parts)


print(humanize_seconds(60 * 60 * 24 * 366 + 60 * 4 + 34))
print(humanize_seconds(60 * 60 * 24))
print(humanize_seconds(60 * 60 * 24 * 14))
print(humanize_seconds(60 * 60 * 24 * 2))
print(humanize_seconds(60 * 60 * 24 * 2.5))
print(humanize_seconds(60 * 60 * 2.5))
print(humanize_seconds(8 * 60 * 2.5))
print(humanize_seconds(8 * 60 * 2.5 + 21))
# print(human_seconds(60 * 60 * 24))
# print("--")
# print(human_seconds(2 * 60 * 60 * 24))
# print("--")
# print(human_seconds(2.5 * 60 * 60 * 24 + 60 *3))
# print("--")
# print(human_seconds(2.5 * 60 * 60 + 60 *3 + 45))
# print("--")
# # print(human_seconds(60 * 60 * 24 + 60 * 60))
