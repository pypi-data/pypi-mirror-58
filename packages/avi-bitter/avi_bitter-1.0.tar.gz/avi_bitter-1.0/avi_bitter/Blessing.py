class Blessing:
    def __init__(self):
        import random
        lines = ['אפילו חמור לא אוכל ככה לפפון על הבוקר', 'אדם זאב לבן אדם, איזה עולם בלי רחמים',
                 'אבי מה הסוד שלך לחיים ארוכים ומצליחים? קפה וסיגריה']
        n = random.randint(0, len(lines) - 1)
        print(lines[n])


import random

lines = ['אפילו חמור לא אוכל ככה לפפון על הבוקר', 'אדם זאב לבן אדם, איזה עולם בלי רחמים',
         'אבי מה הסוד שלך לחיים ארוכים ומצליחים? קפה וסיגריה']
n = random.randint(0, len(lines) - 1)
print(lines[n])
