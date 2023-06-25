from typing import List
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        dic = {}
        for p in positive_feedback:
            dic[p] = 3
        for n in negative_feedback:
            dic[n] = -1

        for i in range(len(report)):
            score = 0
            for word in report[i].split(" "):
                if word in dic:
                    score += dic[word]
            report[i] = score

        temp = sorted(zip(report, student_id), key=lambda e:(-e[0], e[1]))

        return [temp[i][1] for i in range(k)]