#!/usr/bin/python3

def calc_weight(list_=[]):    
    sum_tuples = 0
    weight_ = 0

    if list_ == []:
        return 0
    else:
        for tuple_ in list_:
            sum_tuples += tuple_[0] * tuple_[1]
            weight_ += tuple_[1] 
        return sum_tuples / weight_
 
if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
