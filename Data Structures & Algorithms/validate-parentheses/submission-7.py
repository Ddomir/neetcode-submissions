class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        if len(s) % 2 != 0: return False
        stack = []

        for p in s:
            match p:
                case "(": stack.append(")")
                case "{": stack.append("}")
                case "[": stack.append("]")
                case ")" | "}" | "]": 
                    if not stack or stack.pop() != p: 
                        return False
                case _: return False
        if not stack:
            return True
        else: return False
