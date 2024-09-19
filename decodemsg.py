class Solution:

    def decode(txtfile):

        with open(txtfile, 'r') as file:
            text_lines = file.readlines()
        

        num_word_dict = {}
        for line in text_lines:
            num, word = line.strip().split()
            num_word_dict[int(num)] = word
        
        sorted_nums = sorted(num_word_dict.keys())
        
        message = []
        i = 0
        while True:
            i += 1
            if sum(range(1, i + 1)) > len(sorted_nums):
                break
            end_num = sum(range(1, i + 1))
            message.append(num_word_dict[sorted_nums[end_num - 1]])
        
        return ' '.join(message)

if __name__ == '__main__':
    sol = Solution
    text_file = 'coding_qual_input.txt'
    print(sol.decode(text_file))
    

