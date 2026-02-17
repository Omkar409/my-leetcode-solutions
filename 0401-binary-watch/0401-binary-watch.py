class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for i in range(12):
            hours = format(i,'05b')
            for j in range(60):
                min = format(j,'06b')
                total_lit = hours.count('1')+min.count('1')
                if total_lit == turnedOn:
                    hours_str = str(i)
                    min_str = f"{j:02d}"
                    result.append(f"{hours_str}:{min_str}")
        return result
