import sys
sys.stdin = open('input_12845.txt', 'r')

N = int(input())
cards = list(map(int, input().split()))

max_card = max(cards)
print(max_card * (N - 1) + sum(cards) - max_card)