import os

LISTBOX_MIMETYPE = "application/x-item"

OP_NODE_INPUT = 1
OP_NODE_OUTPUT = 2
OP_NODE_ADD = 3
OP_NODE_SUBTRACT = 4
OP_NODE_MULTIPLY = 5
OP_NODE_DIVIDE = 6

BLOCKS = {
}

BLOCKS_ICONS_PATH = f"{os.path.dirname(__file__)}/../resources/node_icons"

# Way to register by function call
# associateOperationCodeWithBlock(OP_NODE_ADD, AddBlock)


class BlockConfigException(Exception):
    pass


class InvalidNodeRegistration(BlockConfigException):
    pass


class OperationCodeNotRegistered(BlockConfigException):
    pass


def associateOperationCodeWithBlock(operationCode, referenceClass):
    if operationCode in BLOCKS:
        raise InvalidNodeRegistration(f"Duplicite node registration of {operationCode}. "
                                      f"{BLOCKS[operationCode]} already registered.")
    BLOCKS[operationCode] = referenceClass


def registerNode(operationCode):
    def decorator(blockClass):
        associateOperationCodeWithBlock(operationCode, blockClass)
        return blockClass

    return decorator


def getClassFromOperationCode(operationCode):
    if operationCode not in BLOCKS:
        raise OperationCodeNotRegistered(f"{operationCode} is not registered yet.")
    return BLOCKS[operationCode]

# Register blocks
from nodedge.blocks import *
