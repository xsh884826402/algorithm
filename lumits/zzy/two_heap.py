import heapq
#默认小顶堆 大顶堆里面存的是负数


def find_median(nums):
    print(nums)
    min_heap = []
    max_heap = []
    result = []
    max_heap.append(-nums[0])
    result.append(nums[0])
    for num in nums[1:]:
        if len(max_heap) == len(min_heap):
            if num < -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
                tmp = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -tmp)
            result.append(-max_heap[0])
        else:
            if num > max_heap[0]:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappush(max_heap, -num)
                tmp = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, tmp)
            result.append(-max_heap[0])
    return result


def find_median(nums):
    result = []
    max_heap = []
    min_heap = []
    heapq.heappush(max_heap, -nums[0])
    for num in nums[1:]:
        # 无论奇数偶数 都取大顶堆堆顶 n= 7  num = 8 max_heap = 6, 7,扔进小顶堆，从小顶堆拿出，再放进大顶堆，
        if len(max_heap)==len(min_heap):#奇数
            if num < -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
                tmp = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -tmp)
        else:
            # 偶数 ，大顶堆4 小顶堆3个， 8 min_heap 10, max_heap=9  max_heap < target < min_heap
            if num > min_heap[0]:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappush(max_heap, -num)
                tmp = -heapq.heappop(max_heap)
                heapq.heappush(min_heap)

        result.append(-max_heap[0])

    #  tartget > 一堆（大顶堆） target < 一堆（小顶堆)    num1 target, nums2, 大顶堆元素 》= 小顶堆元素的个数5， 3
    return result
# key idea:
#     维护大顶堆和小顶堆，保持大顶堆的元素个数-小顶堆元素的个数=0 or 1
        #大顶堆堆顶 即为 中位数
    #     设大顶堆堆顶为 target， target满足如下条件: 当元素个数为奇数时，大于大顶堆堆顶，小于小顶堆堆顶，则target是我们需求的中位数

# 伪代码：
#     Input: L a1,...an
#     Output: result m1,...mn,其中mi 是ai的 上界[i/2] small元素
#     max_heap := []
#     min_heap := []
#     for num in nums
#         do if len(max_heap)==len(min_heap) # odd
#             then if num < top of max_heap
#                     then max_heap.push(num)
#                 else:
#                     min_heap.push(num)
#                     tmp = min_heap.pop()
#                     max_heap.push(num)
#             else:
#                 xxx

# 正确性证明
# basic k=1 正确；假设k=index，成立，用我的算法去执行，发现index+1也成立；

# 当n=1 时， m1 = a1 正确
# induction hypo: a1,...aj 1<j<=i; m1,...mj, => a1,...aj+1， mj+1也是中位数
# case1， j %2 ==0:  mj 大顶堆和小顶堆的元素个数相同，
#     #                       aj+1
#                                 进入大顶堆 , mj+1,mj+1是第j+1/2 小
#                             aj+1 进入小顶堆，在弹出小顶堆堆顶，再push到大顶堆，mj+1是第j+1/2 小
#     # j%2==1: 大顶堆元素-小顶堆元素个数=1
#                 # 直接进入小顶堆，弹出mj+1,第j+1/2
#                 # 先加入大顶堆，大顶堆弹出 在push进小顶堆，mj+1是第第j+1/2 小
#     mj+1是aj+1的中位数，

#时间复杂度分析
# 最坏的时间
#     3nlogn O(nlogn)
# 1/2 logn+1/2*3lgn 2lgn 2nlgn O(nlogn)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    print(find_median(nums))

# 思路： 通过大顶堆和小顶堆 维护median的左右两侧的数据
# 代码：