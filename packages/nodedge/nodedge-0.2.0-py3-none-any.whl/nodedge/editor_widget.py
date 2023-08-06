from nodedge.scene import Scene, InvalidFile
from nodedge.graphics_view import GraphicsView
from nodedge.node import Node
from nodedge.blocks.block import Block
from nodedge.edge import *
import os


class EditorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__logger = logging.getLogger(__file__)
        self.__logger.setLevel(logging.INFO)

        self.filename = None

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.scene = Scene()
        self.view = GraphicsView(self.scene.graphicsScene, self)
        self.layout.addWidget(self.view)

    def hasName(self):
        return self.filename is not None

    @property
    def shortName(self):
        return os.path.basename(self.filename)

    @property
    def userFriendlyFilename(self):
        name = os.path.basename(self.filename) if self.hasName() else "New graph"
        # TODO: Add * hasBeenModified here
        return name + ("*" if self.isModified() else "")

    def addNodes(self):
        node1 = Node(self.scene, "Node 1", inputSockets=[1, 2, 3], outputSockets=[1])
        node2 = Node(self.scene, "Node 2", inputSockets=[1, 2, 3], outputSockets=[1])
        node3 = Node(self.scene, "Node 3", inputSockets=[1, 2, 3], outputSockets=[1])

        node1.pos = (-350, -250)
        node2.pos = (-75, 100)
        node3.pos = (200, -75)

        edge1 = Edge(self.scene, node1.outputSockets[0], node2.inputSockets[1], edgeType=EDGE_TYPE_BEZIER)
        edge2 = Edge(self.scene, node2.outputSockets[0], node3.inputSockets[2], edgeType=EDGE_TYPE_BEZIER)

        self.scene.history.storeInitialStamp()

    def isModified(self):
        return self.scene.isModified

    @property
    def canUndo(self):
        return self.scene.history.canUndo

    @property
    def canRedo(self):
        return self.scene.history.canRedo

    @property
    def selectedItems(self):
        return self.scene.selectedItems

    def hasSelectedItems(self):
        return self.selectedItems != []

    def updateTitle(self):
        self.setWindowTitle(self.userFriendlyFilename)

    def newFile(self):
        self.scene.clear()
        self.filename = None
        self.scene.history.clear()

    def loadFile(self, filename):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            self.scene.loadFromFile(filename)
            self.filename = filename
            # Don't store initial stamp because the file has still not been changed.
            self.scene.history.clear(storeInitialStamp=False)
            QApplication.restoreOverrideCursor()
            self.evalNodes()
            return True
        except InvalidFile as e:
            self.__logger.warning(f"Error loading {filename}: {e}")
            QApplication.restoreOverrideCursor()
            QMessageBox.warning(self, f"Error loading {os.path.basename(filename)}", str(e))
            return False

    def evalNodes(self):
        for node in self.scene.nodes:
            if isinstance(node, Block):
                node.eval()

    def saveFile(self, filename=None):
        # When called with empty parameter, don't store the filename
        if filename is not None:
            self.filename = filename
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.scene.saveToFile(self.filename)
        QApplication.restoreOverrideCursor()

        return True

