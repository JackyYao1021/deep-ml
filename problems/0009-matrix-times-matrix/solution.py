import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
                m_a = np.array(a)
                m_b = np.array(b)
                try:
                    ans = m_a @ m_b
                    return ans 
                except:
                    return -1