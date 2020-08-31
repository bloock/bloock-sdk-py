from .entity.hash import Hash


class Verifier:

    @staticmethod
    def verify(leaves, nodes, depths, bitmap):
        it_leaves = 0
        it_nodes = 0
        it_bitmap = 0
        curr_bit = 0
        stack = []

        while it_nodes < len(nodes) or it_leaves < len(leaves):
            act_depth = depths[it_nodes + it_leaves]
            is_leaf = (bitmap[it_bitmap] & (1 << (7 - (curr_bit % 8)))) < 1
            curr_bit += 1
            if curr_bit % 8 == 0:
                it_bitmap += 1

            if is_leaf:
                act_hash = leaves[it_leaves]
                it_leaves += 1

            else:
                act_hash = nodes[it_nodes]
                it_nodes += 1

            while stack and stack[len(stack) - 1][1] == act_depth:
                last_hash = stack.pop()
                act_hash = Hash.mergeHex(last_hash[0], act_hash)
                act_depth -= 1
            stack.append((act_hash, act_depth))

        return stack[0][0]

    '''
    # vell
    @staticmethod
    def verify(leaves, nodes, depths, bitmap):
        it_leaves = 0
        it_nodes = 0
        it_bitmap = 0
        curr_bit = 0
        stack = []

        while it_nodes < (len(nodes)-1) or it_leaves < len(leaves):
            act_depth = depths[it_nodes + it_leaves]
            is_leaf = (bitmap[it_bitmap] & (1 << (7 - (curr_bit % 8)))) > 0
            curr_bit += 1

            if is_leaf:
                act_hash = leaves[it_leaves]
                it_leaves += 1

            else:
                act_hash = nodes[it_nodes]
                it_nodes += 1

            while stack and stack[len(stack) - 1][1] == act_depth:
                last_hash = stack.pop()
                act_hash = Hash.mergeHex(last_hash[0], act_hash)
                act_depth -= 1
            stack.append((act_hash, act_depth))

        return Hash.identicalKeys(stack[0][0], nodes[it_nodes])
    '''
