from nodedge.blocks.block import *
from nodedge.blocks.block_config import registerNode, OP_NODE_ADD, BLOCKS_ICONS_PATH


@registerNode(OP_NODE_ADD)
class AddBlock(Block):
    icon = f"{BLOCKS_ICONS_PATH}/add.png"
    operationCode = OP_NODE_ADD
    operationTitle = "Add"
    contentLabel = "+"
    contentLabelObjectName = "BlockBackground"

    def evalImplementation(self):
        i0 = self.inputNodeAt(0)
        i1 = self.inputNodeAt(1)

        try:
            result = i0.eval() + i1.eval()
        except TypeError as e:
            raise EvaluationError(e)

        self.value = result

        return self.value
