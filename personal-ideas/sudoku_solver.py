class Box:
    def __init__(self, row, column):
        self.answer = None
        self.candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.row = row
        self.column = column
        self.square = ((column // 3) + 1) + ((row // 3) * 3)


'''
strategies

1. eliminate all candidates based on numbers present at start of game (eliminate from row, column, and box (RCB)
2. scan the board for boxes with 1 candidate. do until one full pass of board w/0 single candidate box
3. scan RCB for boxes that have a candidate that none other has (fill that box perform step 1) (redo step 2 and then do step 3 until a full pass with no success?)
4. scan RCB for sets of boxes that have a pair of unique candidates (eliminate the pair of candidates for RCB) (step 2,3,4 until full unsuccessful pass)
5. limit of model
'''
