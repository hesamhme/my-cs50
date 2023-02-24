def main():

 print("what is the anserw to the Great Question of Life, the Universe and Everything? ")
 anw = condition(input('>>>'))
def condition(x):
 if x.strip() == '42' :
    print('yes')
 elif x.lower().strip() == 'forty two':
    print('yes')
 elif x.lower().strip() =='forty-two':
    print('yes')
 else:
    print('No')
main()