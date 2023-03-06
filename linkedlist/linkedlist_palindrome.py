from linkedlist.linkedlist_utils import *
from linkedlist.linkedlist_reverse import *


def build_linkedlist(nums):
    nodes = []
    for num in nums:
        nodes.append(Node(num))
    for i, node in enumerate(nodes[:-1]):
        node.right = nodes[i+1]
    return nodes


# def if_palindrome_linkedlist(root):
#     # 先按照奇数写，再对照偶数
#     # 找到中间node
#     mid = find_mid_node(root)
#
#     # 翻转右半部分
#     right_part_last = reverse_one_direction_node(mid)
#     temp = right_part_last
#     # 从两侧向中间比对，判断是否回文
#     result = True
#     left_part_first = root
#     while left_part_first and right_part_last:
#         if left_part_first.val != right_part_last.val:
#             result = False
#             break
#         left_part_first = left_part_first.right
#         right_part_last = right_part_last.right
#
#     # 复原右半部分
#     reverse_one_direction_node(temp)
#     return result


def if_palindrome_linkedlist(root):
    # 先按照奇数写，再对照偶数
    # 找到中间node
    mid = find_mid_node(root)

    # 翻转右半部分
    right_part_last = reverse_one_direction_node(mid)

    # 从两侧向中间比对，判断是否回文
    result = True
    left_tmp = root
    right_tmp = right_part_last
    while left_tmp and right_tmp:
        if left_tmp.val != right_tmp.val:
            result = False
            break
        left_tmp = left_tmp.right
        right_tmp = right_tmp.right
    # 复原右半部分
    reverse_one_direction_node(right_part_last)
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 1]
    nodes = build_linkedlist(nums)
    if len(nums)==0:
        print('True')
    else:
        print(if_palindrome_linkedlist(nodes[0]))
        show_nodes(nodes[0])
