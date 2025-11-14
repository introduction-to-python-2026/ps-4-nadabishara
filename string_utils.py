def split_at_first_digit(formula):
    digit_location = 1

    for char in formula[1 : ] :

      if char.isdigit():
        break

      digit_location += 1

    if digit_location == len(formula) :
      return formula , 1

    else :
      prefix = formula [ :digit_location]
      number = int (formula[digit_location: ])
      return prefix,number



def split_at_first_digit(formula):
    pass # Replace the `pass` with your code
