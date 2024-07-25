# 아래 클래스를 수정하시오.
class StringRepeater:
    
    def __init__(self):
        pass
        
    @classmethod
    def repeat_string(cls, rep_num, rep_str):
        for i in range(int(rep_num)):
            print(f'{rep_str}')
        


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
