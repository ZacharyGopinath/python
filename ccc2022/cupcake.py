# finished question

R = input()
S = input()
def cupcake(R, S):
    num_cupcakes = (int(R) * 8) + (int(S) * 3)
    return num_cupcakes - 28
print(cupcake(R, S))

#regular 8
#small 3
#total ppl 28
#(2, 5) => 3