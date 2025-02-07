'''
Function
'''

def calculateArea (l,b): 

'''def: यो calculateArea नामको function define गर्न प्रयोग गरिएको
 छ। l, b: यी दुई parameters (लम्बाइ र चौडाइ) हुन्, जुन function लाई  दिइन्छ।'''
    
    a = l * b  # क्षेत्रफल निकाल्न लम्बाइ र चौडाइलाई गुणन गरिन्छ
    return a  #  return a: गणना गरिएको क्षेत्रफल function बाट फिर्त गर्छ।

print (f'area is {calculateArea (10,5)}')

''' calculateArea(10,5) लाई call गर्दा l = 10 र b = 5 हुन जान्छ।
10 * 5 = 50 भएर function ले 50 फिर्ता गर्छ।
अन्तिममा, print(f'area is {50}') हुँदा Output:50'''
    
    
def calculateVol (l,b,h):
    v = l * b * h
    return v

print (f'volume is {calculateVol(10,4,2)}')
