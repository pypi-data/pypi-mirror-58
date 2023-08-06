import re
import time
from anytree import AnyNode, RenderTree, PreOrderIter


def _is_rightest_child(node):
    if len(node.siblings) > 0:
        for sibling in node.siblings:
            rightest = 1
            if sibling.N > node.N:
                rightest = 0
    elif len(node.siblings) == 0 and node.id != 'root':
        rightest = 1
    else:
        rightest = 0

    return rightest


def _has_children(node):
    return bool(len(node.children))


def _get_tabs(level):
    key = {0: '',
           1: '\t',
           2: '\t\t',
           3: '\t\t\t',
           4: '\t\t\t\t',
           5: '\t\t\t\t\t',
           6: '\t\t\t\t\t\t',
           7: '\t\t\t\t\t\t\t',
           8: '\t\t\t\t\t\t\t\t',
           9: '\t\t\t\t\t\t\t\t\t'}

    return key[level]


def _get_parent(child, parent_type):
    for node in child.ancestors:
        if parent_type.lower() in node.id:
            return node


def _get_block(node):
    if node.type == 'page':
        block = ['*BeginPage() // Page ' + node.page_num, '*EndPage()']

    elif node.type == 'sessiontitle':
        block = [_get_tabs(node.level) + '# Session Title : ' + node.data]

    elif node.type == 'graphics_files':
        block = ['{ GRAPHIC_FILE_' + str(node.instance) + ' = "' + node.data[node.instance] + '"}']

    elif node.type == 'results_files':
        block = ['{ RESULT_FILE_' + str(node.instance) + ' = "' + node.data[node.instance] + '"}']

    elif node.type == 'active':
        block = [_get_tabs(node.level) + '*IsActive()']

    elif node.type == 'name':
        block = [_get_tabs(node.level) + '*Name("' + node.data + ' ' + node.page_num + '")']

    elif node.type == 'title':
        block = [_get_tabs(node.level) + '*Title("' + node.data + '", On)']

    elif node.type == 'titlefont':
        font = node.data
        block = [_get_tabs(node.level) + '*TitleFont("' + str(font[0]) + \
                 '", ' + str(font[1]) + ', ' + str(font[2]) + ', ' + str(font[3]) + ')']

    elif node.type == 'layout':
        block = [_get_tabs(node.level) + '*Layout(' + node.data + ')']

    elif node.type == 'root':
        block = ['{ safe_quotes_on }' + '\n' + '*Id("' + node.gui + '", "' + str(node.version) + '.*")', '']

    elif node.type == 'palette':
        block = ['*BeginPalette()', '*EndPalette()']

    elif node.type == 'animator':
        block = [_get_tabs(node.level) + '*BeginAnimator(' + node.data + ')',
                 _get_tabs(node.level) + '*EndAnimator()']

    elif node.type == 'window':
        block = [_get_tabs(node.level) + '*BeginWindow(Animation)         // Window ' + str(node.window_num),
                 _get_tabs(node.level) + '*EndWindow()']

    elif node.type == 'exportformat':
        block = [_get_tabs(node.level) + '*ExportFormat("' + node.data + '")']

    elif node.type == 'graphic':
        block = [_get_tabs(node.level) + '*BeginGraphic()',
                 _get_tabs(node.level) + '*EndGraphic()']

    elif node.type == 'lightinfo':
        block = [_get_tabs(node.level) + '*LightInfo(' + node.data + ')']

    elif node.type == 'rotationangle':
        block = [_get_tabs(node.level) + '*RotationAngle(' + node.data + ')']

    elif node.type == 'model':
        block = [_get_tabs(node.level) + '*BeginModel({GRAPHIC_FILE_' + str(node.data) + '})',
                 _get_tabs(node.level) + '*EndModel()']

    elif node.type == 'savedview':
        block = [_get_tabs(node.level) + '*BeginSavedView("' + str(node.data) + '")',
                 _get_tabs(node.level) + '*EndSavedView()']

    elif node.type == 'projectiontype':
        block = [_get_tabs(node.level) + '*ProjectionType("' + node.data + '")']

    elif node.type == 'view':
        block = [_get_tabs(node.level) + '*View("' + node.data + '")']

    elif node.type == 'clippingregion':
        block = [_get_tabs(node.level) + '*ClippingRegion("' + node.data + '")']

    elif node.type == 'result':
        block = [_get_tabs(node.level) + '*BeginResult({RESULT_FILE_' + str(node.data) + '})',
                 _get_tabs(node.level) + '*EndResult()']

    elif node.type == 'currentposition':
        block = [_get_tabs(node.level) + '*CurrentPosition(' + node.data + ')']

    elif node.type == 'numbersteps':
        block = [_get_tabs(node.level) + '*NumberOfSteps(' + node.data + ')']

    elif node.type == 'increment':
        block = [_get_tabs(node.level) + '*Increment(' + node.data + ')']

    elif node.type == 'colorby':
        block = [_get_tabs(node.level) + '*ColorBy("' + node.data + '")']

    elif node.type == 'color':
        block = [_get_tabs(node.level) + '*Color("' + node.data + '")']

    elif node.type == 'gradientcolor':
        block = [_get_tabs(node.level) + '*GradientColor("' + node.data + '")']

    elif node.type == 'smalldeformation':
        block = [_get_tabs(node.level) + '*SmallDeformation("' + node.data + '")']

    elif node.type == 'currentsubcase':
        block = [_get_tabs(node.level) + '*CurrentSubcase(' + node.data + ')']

    elif node.type == 'part':
        block = [_get_tabs(node.level) + '*BeginPart(' + node.data + ')', _get_tabs(node.level) + '*EndPart()']

    elif node.type == 'attribute':
        block = [_get_tabs(node.level) + '*Attribute(' + node.data + ')']

    elif node.type == 'contour':
        block = [_get_tabs(node.level) + '*BeginContour(' + node.data + ')', _get_tabs(node.level) + '*EndContour()']

    elif node.type == 'displayoptions':
        block = [_get_tabs(node.level) + '*DisplayOptions(' + node.data + ')']

    elif node.type == 'contourselection':
        block = [_get_tabs(node.level) + '*BeginSelection(' + node.data + ')',
                 _get_tabs(node.level) + '*EndSelection()']

    elif node.type == 'contourselectionadd':
        block = [_get_tabs(node.level) + '*Add("' + node.data + '")']

    elif node.type == 'group':
        block = [_get_tabs(node.level) + '*BeginGroup(' + node.data + ')', _get_tabs(node.level) + '*EndGroup()']

    elif node.type == 'groupselection':
        block = [_get_tabs(node.level) + '*BeginSelection(' + node.data + ')',
                 _get_tabs(node.level) + '*EndSelection()']

    elif node.type == 'dimension':
        block = [_get_tabs(node.level) + '*Add("dimension == ' + node.data + '")']

    elif node.type == 'selection':
        block = [_get_tabs(node.level) + '*BeginSelection(' + node.data + ')',
                 _get_tabs(node.level) + '*EndSelection()']

    elif node.type == 'groupselectionadd':
        block = [_get_tabs(node.level) + '*Add("' + node.data + '")']

    elif node.type == 'resulttype':
        block = [_get_tabs(node.level) + '*ResultType("' + node.data + '")']

    elif node.type == 'datacomponent':
        block = [_get_tabs(node.level) + '*DataComponent("' + node.data + '")']

    elif node.type == 'multiplelayers':
        block = [_get_tabs(node.level) + '*MultipleLayers("' + node.data + '")']

    elif node.type == 'layer':
        block = [_get_tabs(node.level) + '*Layer("' + node.data + '")']

    elif node.type == 'layerfilter':
        block = [_get_tabs(node.level) + '*LayerFilter(' + node.data + ')']

    elif node.type == 'complexfilter':
        block = [_get_tabs(node.level) + '*ComplexFilter("' + node.data + '")']

    elif node.type == 'resolvedinsystem':
        block = [_get_tabs(node.level) + '*ResolvedInSystem(' + node.data + ')']

    elif node.type == 'averagingmethod':
        block = [_get_tabs(node.level) + '*AveragingMethod(' + node.data + ')']

    elif node.type == 'averageacrossparts':
        block = [
            _get_tabs(node.level) + '*AverageAcrossParts(' + node.data + ')']

    elif node.type == 'showmidsidenoderesults':
        block = [_get_tabs(node.level) + '*ShowMidsideNodeResults(' + node.data + ')']

    elif node.type == 'featureangleaverage':
        block = [
            _get_tabs(node.level) + '*FeatureAngleAverage(' + node.data + ')']

    elif node.type == 'averagecolor':
        block = [_get_tabs(node.level) + '*AverageColor(' + node.data + ')']

    elif node.type == 'discretecolor':
        block = [_get_tabs(node.level) + '*DiscreteColor(' + node.data + ')']

    elif node.type == 'legendminthreshold':
        block = [_get_tabs(node.level) + '*LegendMinThreshold(' + str(node.data) + ')']

    elif node.type == 'legendmaxthreshold':
        block = [_get_tabs(node.level) + '*LegendMaxThreshold(' + str(node.data) + ')']

    elif node.type == 'legend':
        block = [_get_tabs(node.level) + '*BeginLegend(' + node.data + ')',
                 _get_tabs(node.level) + '*EndLegend()']

    elif node.type == 'legendtype':
        block = [_get_tabs(node.level) + '*LegendType("' + node.data + '")']

    elif node.type == 'numcols':
        block = [_get_tabs(node.level) + '*NumCols(' + node.data + ')']
    
    elif node.type == 'colorrgb':
        block = [_get_tabs(node.level) + '*ColorRGB(' + node.data + ')']

    elif node.type == 'noresultcolor':
        block = [_get_tabs(node.level) + '*NoResultColor("' + node.data + '")']
    
    elif node.type == 'numbers':
        block = [_get_tabs(node.level) + '*Numbers(' + node.data + ')']
    
    elif node.type == 'showmax':
        block = [_get_tabs(node.level) + '*ShowMax("' + node.data + '")']
    
    elif node.type == 'showmaxlocal':
        block = [_get_tabs(node.level) + '*ShowMaxLocal("' + node.data + '")']

    elif node.type == 'showmin':
        block = [_get_tabs(node.level) + '*ShowMin("' + node.data + '")']

    elif node.type == 'showminlocal':
        block = [_get_tabs(node.level) + '*ShowMinLocal("' + node.data + '")']
    
    elif node.type == 'entitylabel':
        block = [_get_tabs(node.level) + '*EntityLabel("' + node.data + '")']
    
    elif node.type == 'showbymodel':
        block = [_get_tabs(node.level) + '*ShowByModel("' + node.data + '")']
    
    elif node.type == 'legendposition':
        block = [_get_tabs(node.level) + '*LegendPosition("' + node.data + '")']
        
    elif node.type == 'backgroundcolor':
        block = [_get_tabs(node.level) + '*BackGroundColor("' + node.data + '")']
    
    elif node.type == 'transparency':
        block = [_get_tabs(node.level) + '*Transparency("' + node.data + '")']
    
    elif node.type == 'filter':
        block = [_get_tabs(node.level) + '*Filter("' + node.data + '")']

    elif node.type == 'note':
        block = [_get_tabs(node.level) + '*BeginNote(' + node.data + ')',
                 _get_tabs(node.level) + '*EndNote()']
    
    elif node.type == 'transparent':
        block = [_get_tabs(node.level) + '*Transparent("' + node.data + '")']

    elif node.type == 'autohide':
        block = [_get_tabs(node.level) + '*AutoHide("' + node.data + '")']
    
    elif node.type == 'anchortoscreen':
        block = [_get_tabs(node.level) + '*AnchorToScreen("' + node.data + '")']
    
    elif node.type == 'fillcolor':
        block = [_get_tabs(node.level) + '*FillColor(' + node.data + ')']
    
    elif node.type == 'textcolor':
        block = [_get_tabs(node.level) + '*FillColor(' + node.data + ')']
    
    elif node.type == 'attach':
        block = [_get_tabs(node.level) + '*Attach("' + node.data + '")']
    
    elif node.type == 'position':
        block = [_get_tabs(node.level) + '*Position(' + node.data + ')']
    
    elif node.type == 'text':
        block = [_get_tabs(node.level) + '*Text("' + node.data + '")']
    
    elif node.type == 'font':
        block = [_get_tabs(node.level) + '*Font(' + node.data + ')']
    
    elif node.type == 'color':
        block = [_get_tabs(node.level) + '*Color(' + node.data + ')']
    
    elif node.type == 'borderwidth':
        block = [_get_tabs(node.level) + '*BorderWidth(' + node.data + ')']
    
    elif node.type == 'shape':
        block = [_get_tabs(node.level) + '*Shape("' + node.data + '")']
    
    elif node.type == 'notealignment':
        block = [_get_tabs(node.level) + '*NoteAlignment("' + node.data + '")']
    
    elif node.type == 'noteanchor':
        block = [_get_tabs(node.level) + '*NoteAnchor(' + node.data + ')']
    
    elif node.type == 'titleflag':
        block = [_get_tabs(node.level) + '*TitleFlag("' + node.data + '")']

    elif node.type == 'deformed':
        block = [_get_tabs(node.level) + '*BeginDeformed(' + node.data + ')',
                 _get_tabs(node.level) + '*EndDeformed()']
    
    elif node.type == 'scalemode':
        block = [_get_tabs(node.level) + '*ScaleMode("' + node.data + '")']

    elif node.type == 'scale':
        block = [_get_tabs(node.level) + '*Scale("' + node.data + '")']

    elif node.type == 'resolvedinsystem':
        block = [_get_tabs(node.level) + '*ResolvedInSystem(' + node.data + ')']

    elif node.type == 'undeformedmode':
        block = [_get_tabs(node.level) + '*UndeformedMode("' + node.data + '")']

    elif node.type == 'undeformedcolor':
        block = [_get_tabs(node.level) + '*UndeformedColor("' + node.data + '")']

    elif node.type == 'undeformedtracking':
        block = [_get_tabs(node.level) + '*UndeformedTracking("' + node.data + '")']
        
    else:
        pass

    return block


def _update_layout(page, configuration):
    temp = re.findall(r'\d+', page.id)  # get integers from id
    page_num = ''.join(temp)  # make a number out of all found integers. Works only when id = name + i

    for node in page.children:

        if 'layout' + page_num in node.id:
            node.data = str(configuration)

    return page


def _is_valid_window_configuration(windows, configuration):

    if windows == 1 and configuration == 1:
        return True
    elif windows == 2 and configuration == 2:
        return True
    elif windows == 2 and configuration == 3:
        return True
    elif windows == 3 and configuration == 4:
        return True
    elif windows == 3 and configuration == 5:
        return True
    elif windows == 3 and configuration == 6:
        return True
    elif windows == 3 and configuration == 7:
        return True
    elif windows == 3 and configuration == 8:
        return True
    elif windows == 3 and configuration == 9:
        return True
    elif windows == 4 and configuration == 10:
        return True
    elif windows == 6 and configuration == 11:
        return True
    elif windows == 6 and configuration == 12:
        return True
    elif windows == 9 and configuration == 13:
        return True
    elif windows == 12 and configuration == 14:
        return True
    elif windows == 12 and configuration == 15:
        return True
    elif windows == 16 and configuration == 16:
        return True
    elif windows == 4 and configuration == 17:
        return True
    elif windows == 8 and configuration == 18:
        return True
    elif windows == 4 and configuration == 19:
        return True
    elif windows == 8 and configuration == 20:
        return True
    else:
        return False


def _is_valid_contour(resulttype, datacomponent):
    key = {'Displacement':('Mag','X','Y','Z'),
           'Element Stresses (2D & 3D)':('Absolute Max Principal','vonMises')
    }
    if datacomponent in key[resulttype]:
        return True
    else:
        return False


def _global_callback(name, mod):
    
    if isinstance(mod[0], AnyNode):
        node = mod[0]
        data = mod[1]
        node.data = data

    # elif str(mod[0]).isdigit():
    #     contour_num = str(mod[0])
    #     data = str(mod[1])
    #     for node in PreOrderIter(root):#add root node input to this function
    #         if node.id == name + contour_num:
    #             node.data = data
    #             break
    else:
        print('\n:: Error :: ' + mod[0] + ' is not a valid input.')
        quit()
        
    return


class PageState(object):

    def __init__(self, gui, version, graphics, results, **kwargs):
        self._gui = gui
        self._version = version
        self._graphics = graphics
        self._results = results
        self._name = 'Template'
        self._sessiontitle = 'AutoSession 1'
        self._title = 'Untitled'
        self._animator = 'Static'
        self._titlefont = ('Arial', 1, 0, 12)

        self._observers_gui = []
        self._observers_version = []
        self._observers_graphics = []
        self._observers_results = []
        self._observers_name = []
        self._observers_sessiontitle = []
        self._observers_title = []
        self._observers_animator = []
        self._observers_titlefont = []

    @property  # getter for sessiontitle State attribute
    def sessiontitle(self):  # new getter property for every variable that is observed
        return self._sessiontitle

    @sessiontitle.setter  # setter for sessiontitle State attribute
    def sessiontitle(self, data):
        self._sessiontitle = data
        for callback in self._observers_sessiontitle:
            callback(self._sessiontitle)

    @property  # getter for sessiontitle State attribute
    def title(self):  # new getter property for every variable that is observed
        return self._sessiontitle

    @title.setter  # setter for sessiontitle State attribute
    def title(self, data):
        self._title = data
        for callback in self._observers_title:
            callback(self._title)

    @property  # getter for sessiontitle State attribute
    def titlefont(self):  # new getter property for every variable that is observed
        return self._sessiontitle

    @titlefont.setter  # setter for sessiontitle State attribute
    def titlefont(self, data):
        self._titlefont = data
        for callback in self._observers_titlefont:
            callback(self._titlefont)

    @property  # getter for sessiontitle State attribute
    def animator(self):  # new getter property for every variable that is observed
        return self._animator

    @animator.setter  # setter for sessiontitle State attribute
    def animator(self, data):
        self._animator = data
        for callback in self._observers_animator:
            callback(self._animator)

    @property  # getter for sessiontitle State attribute
    def graphics(self):  # new getter property for every variable that is observed
        return self._graphics

    @graphics.setter  # setter for sessiontitle State attribute
    def graphics(self, data):
        self._graphics = data
        for callback in self._observers_graphics:
            callback(self._graphics)

    @property  # getter for sessiontitle State attribute
    def results(self):  # new getter property for every variable that is observed
        return self._results

    @results.setter  # setter for sessiontitle State attribute
    def results(self, data):
        self._results = data
        for callback in self._observers_results:
            callback(self._results)

    def bind_to_gui(self, callback):  # Bind property to Template method
        self._observers_gui.append(callback)

    def bind_to_version(self, callback):  # Bind property to Template method
        self._observers_version.append(callback)

    def bind_to_graphics(self, callback):  # Bind property to Template method
        self._observers_graphics.append(callback)

    def bind_to_results(self, callback):  # Bind property to Template method
        self._observers_results.append(callback)

    def bind_to_name(self, callback):  # Bind property to Template method
        self._observers_name.append(callback)

    def bind_to_sessiontitle(self, callback):  # Bind property to Template method
        self._observers_sessiontitle.append(callback)

    def bind_to_title(self, callback):  # Bind property to Template method
        self._observers_title.append(callback)

    def bind_to_animator(self, callback):  # Bind property to Template method
        self._observers_animator.append(callback)

    def bind_to_titlefont(self, callback):  # Bind property to Template method
        self._observers_titlefont.append(callback)


class Page(object):

    def __init__(self, data, **kwargs):
        self.data = data
        self.data.bind_to_sessiontitle(self.modify_sessiontitle)
        self.data.bind_to_title(self.modify_title)
        self.data.bind_to_graphics(self.modify_graphics)
        self.data.bind_to_results(self.modify_results)
        self.data.bind_to_animator(self.modify_animator)
        self.data.bind_to_titlefont(self.modify_titlefont)

        self.root = AnyNode(id='root', type='root', oc=1, level=0, gui=data._gui, version=data._version,
                            page_num=str(0), N=0, parent=None)  # add header
        self.treevisual = RenderTree(self.root)
        self.pagename = 'Page'
        self.layout = '1'
        self.currentposition = '25'
        self.numbersteps = '25'
        self.increment = 'Forward, Frame, 1, BounceOff'

        self.title = self.data._title
        self.titlefont = self.data._titlefont
        self.animator = self.data._animator

        self.add_sessiontitle(data.sessiontitle)  # add default nodes
        self.add_graphics(data.graphics)
        self.add_results(data.results)
        self.add_palette()

    def add_sessiontitle(self, sessiontitle):
        type = 'sessiontitle'
        name = type
        node = AnyNode(id=name, type=type, oc=1, parent=self.root, data=sessiontitle,
                       level=None, page_num=str(0), N=None, position=None)
        node.level = len(node.ancestors) - 1
        node.N = len(self.root.leaves)

    def add_graphics(self, graphics):
        for i in range(len(graphics)):  # add graphics files
            type = 'graphics_files'
            name = type + str(i)
            node = AnyNode(id=name, type=type, oc=1, parent=self.root, data=graphics,
                           level=None, N=None, position=None, instance=i)
            node.level = len(node.ancestors) - 1
            node.N = len(self.root.leaves)

    def add_results(self, results):
        for i in range(len(results)):  # add result files. can be any solver output database
            type = 'results_files'
            name = type + str(i)
            node = AnyNode(id=name, type=type, oc=1, parent=self.root, data=results,
                           level=None, N=None, position=None, instance=i)
            node.level = len(node.ancestors) - 1
            node.N = len(self.root.leaves)

    def add_palette(self):

        type = 'palette'
        name = type  # add palette. not sure what this does in HV
        node = AnyNode(id=name, type=type, parent=self.root, level=None,
                       N=None, position=None)
        node.level = len(node.ancestors) - 1
        node.N = len(self.root.leaves)

    def add_pages(self, num_pages, **kwargs):

        allowed_keys = {'title', 'pagename', 'titlefont', 'animator'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

        class PageAttributes(object):
            Root = AnyNode(id=None, type=None, parent=None, level=None, page_num=None, N=None)
            Active = AnyNode(id=None, type=None, oc=None, parent=None, level=None, page_num=None, N=None)
            Name = AnyNode(id=None, type=None, oc=None, parent=None, level=None, data=None, page_num=None, N=None)
            Title = AnyNode(id=None, type=None, oc=None, parent=None, level=None, data=None, page_num=None, N=None)
            TitleFont = AnyNode(id=None, type=None, oc=None, parent=None, level=None, data=None, page_num=None, N=None)
            Layout = AnyNode(id=None, type=None, oc=None, parent=None, level=None, data=None, page_num=None, N=None)
            Animator = AnyNode(id=None, type=None, oc=None, parent=None, level=None, data=None, page_num=None, N=None)
            CurrentPosition = AnyNode(id=None, type=None, oc=None, parent=None, level=None, data=None, page_num=None,
                                      N=None)
            NumberSteps = AnyNode(id=None, type=None, oc=None, parent=None, level=None, data=None, page_num=None,
                                  N=None)
            Increment = AnyNode(id=None, type=None, oc=None, parent=None, level=None, data=None, page_num=None, N=None)

        Page = [PageAttributes() for i in range(num_pages)]

        for i in range(num_pages):  # add all pages
            page_i = str(i)

            type = 'page'
            name = type + page_i
            Page[i].Root = AnyNode(id=name, type=type, parent=self.root,
                                   level=None, page_num=page_i, N=None)
            Page[i].Root.level = len(Page[i].Root.ancestors) - 1
            Page[i].Root.N = len(self.root.leaves)

            type = 'active'
            name = type + page_i
            Page[i].Active = AnyNode(id=name, type=type, oc=1, parent=Page[i].Root,
                                     level=None, page_num=page_i, N=None)
            Page[i].Active.level = len(Page[i].Root.ancestors)
            Page[i].Active.N = len(self.root.leaves)

            type = 'name'
            name = type + page_i
            level = len(Page[i].Root.ancestors)
            Page[i].Name = AnyNode(id=name, type=type, oc=1, parent=Page[i].Root,
                                   level=level, data=self.pagename, page_num=page_i, N=None)
            Page[i].Name.N = len(self.root.leaves)

            type = 'title'
            name = type + page_i
            Page[i].Title = AnyNode(id=name, type=type, oc=1, parent=Page[i].Root,
                                    level=None, data=self.title, page_num=page_i, N=None)
            Page[i].Title.level = len(Page[i].Root.ancestors)
            Page[i].Title.N = len(self.root.leaves)

            type = 'titlefont'
            name = type + page_i
            Page[i].TitleFont = AnyNode(id=name, type=type, oc=1,
                                        parent=Page[i].Root,
                                        level=None,
                                        data=self.titlefont, page_num=page_i, N=None)
            Page[i].TitleFont.level = len(Page[i].Root.ancestors)
            Page[i].TitleFont.N = len(self.root.leaves)

            type = 'layout'
            name = type + page_i
            Page[i].Layout = AnyNode(id=name, type=type, oc=1, parent=Page[i].Root,
                                     level=None, data=self.layout, page_num=page_i, N=None)
            Page[i].Layout.level = len(Page[i].Root.ancestors)
            Page[i].Layout.N = len(self.root.leaves)

            type = 'animator'
            name = type + page_i
            Page[i].Animator = AnyNode(id=name, type=type,
                                       parent=Page[i].Root,
                                       level=None, data=self.animator, page_num=page_i, N=None)
            Page[i].Animator.level = len(Page[i].Root.ancestors)
            Page[i].Animator.N = len(self.root.leaves)

            type = 'currentposition'
            name = type + page_i
            Page[i].CurrentPosition = AnyNode(id=name, type=type,
                                              parent=Page[i].Animator,
                                              level=None, data=self.currentposition,
                                              page_num=page_i, N=None)
            Page[i].CurrentPosition.level = len(Page[i].Animator.ancestors)
            Page[i].CurrentPosition.N = len(self.root.leaves)

            type = 'numbersteps'
            name = type + page_i
            Page[i].NumberSteps = AnyNode(id=name, type=type,
                                          parent=Page[i].Animator,
                                          level=None, data=self.numbersteps,
                                          page_num=page_i, N=None)
            Page[i].NumberSteps.level = len(Page[i].Animator.ancestors)
            Page[i].NumberSteps.N = len(self.root.leaves)

            type = 'increment'
            name = type + page_i
            Page[i].Increment = AnyNode(id=name, type=type,
                                        parent=Page[i].Animator,
                                        level=None, data=self.increment,
                                        page_num=page_i, N=None)
            Page[i].Increment.level = len(Page[i].Animator.ancestors)
            Page[i].Increment.N = len(self.root.leaves)

        return Page

    def modify_palette(self):

        pass

    def modify_results(self, results):#xxx
        instance = 0
        for node in PreOrderIter(self.root):
            if 'results_files' in node.id:
                node.data = [results[instance]]
                instance = instance + 1

    def modify_graphics(self, graphics):#xxx

        for node in PreOrderIter(self.root):
            if node.id == 'graphics_files':
                node.data = graphics
                break

    def modify_sessiontitle(self, sessiontitle):#xxx

        for node in PreOrderIter(self.root):
            if node.id == 'sessiontitle':
                node.data = sessiontitle
                break

    def modify_title(self, page_mod):
        _global_callback('title', page_mod)

    def modify_animator(self, page_mod):
        _global_callback('animator', page_mod)

    def modify_titlefont(self, page_mod):
        _global_callback('titlefont', page_mod)

        return


class WindowState(object):

    def __init__(self, **kwargs):
        self._exportformat = 'PNG'

        self._observers_exportformat = []

    @property  # getter for sessiontitle State attribute
    def exportformat(self):  # new getter property for every variable that is observed
        return self._exportformat

    @exportformat.setter  # setter for sessiontitle State attribute
    def exportformat(self, data):
        self._exportformat = data
        for callback in self._observers_exportformat:
            callback(self._exportformat)

    def bind_to_exportformat(self, callback):  # Bind property to Template method
        self._observers_exportformat.append(callback)


class Window(object):

    def __init__(self, data, **kwargs):
        self.data = data
        self.data.bind_to_exportformat(self.modify_exportformat)

        self.exportformat = self.data._exportformat

    def add_windows(self, num_windows, page, configuration, **kwargs):
        self.Page_i = page
        self.root = page.root
        allowed_keys = {'exportformat'}
        if _is_valid_window_configuration(num_windows, configuration):
            self.Page_i = _update_layout(self.Page_i, configuration)
        else:
            print('***ERROR: INVALID NUMBER OF WINDOWS AND/OR CONFIGURATION.\n')
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

        class WindowAttributes(object):
            Root = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None)]
            Active = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ExportFormat = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            AnimationNote = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]

        Window = [WindowAttributes() for i in range(num_windows)]

        for i in range(num_windows):  # add all pages
            window_i = str(i)

            type = 'window'
            name = type + window_i
            Window[i].Root = AnyNode(id=name, type=type, parent=self.Page_i,
                                     level=None, window_num=window_i)
            Window[i].Root.level = len(Window[i].Root.ancestors) - 1
            Window[i].Root.N = len(self.root.leaves)

            type = 'active'
            name = type + window_i
            Window[i].Active = AnyNode(id=name, type=type, oc=1, parent=Window[i].Root,
                                       level=None, window_num=window_i, N=None)
            Window[i].Active.level = len(Window[i].Root.ancestors)
            Window[i].Active.N = len(self.root.leaves)

            type = 'exportformat'
            name = type + window_i
            Window[i].ExportFormat = AnyNode(id=name, type=type, oc=1, parent=Window[i].Root,
                                             level=None, window_num=window_i, N=None, data=self.exportformat)
            Window[i].ExportFormat.level = len(Window[i].Root.ancestors)
            Window[i].ExportFormat.N = len(self.root.leaves)

        return Window

    def modify_exportformat(self, window_mod):
        _global_callback('exportformat', window_mod)


class GraphicState(object):

    def __init__(self, **kwargs):
        self._lightinfo = '0, 0, 1, 0, 0, 0, 64'
        self._rotationangle = '15'
        self._savedview = 'Current View'
        self._projectiontype = 'Orthographic'
        self._view = '0.707107 0.353553 -0.612372 0.000000 -0.707107 0.353553 -0.612372 0.000000 0.000000 0.866025 0.500000 0.000000 0.000000 0.000000 0.000000 1.000000'
        self._clippingregion = '-5.585992 6.464380 -2.172861 9.613941 -6.588268 2.100116'
        # xxx Write function to get good defaulf view
        # xxx Write function to get good clipping region

        self._observers_lightinfo = []
        self._observers_rotationangle = []
        self._observers_savedview = []
        self._observers_projectiontype = []
        self._observers_view = []
        self._observers_clippingregion = []

    @property  # getter for sessiontitle State attribute
    def lightinfo(self):  # new getter property for every variable that is observed
        return self._lightinfo

    @lightinfo.setter  # setter for sessiontitle State attribute
    def lightinfo(self, data):
        self._lightinfo = data
        for callback in self._observers_lightinfo:
            callback(self._lightinfo)

    @property  # getter for sessiontitle State attribute
    def rotationangle(self):  # new getter property for every variable that is observed
        return self._rotationangle

    @rotationangle.setter  # setter for sessiontitle State attribute
    def rotationangle(self, data):
        self._rotationangle = data
        for callback in self._observers_rotationangle:
            callback(self._rotationangle)

    @property  # getter for sessiontitle State attribute
    def savedview(self):  # new getter property for every variable that is observed
        return self._savedview

    @savedview.setter  # setter for sessiontitle State attribute
    def savedview(self, data):
        self._savedview = data
        for callback in self._observers_savedview:
            callback(self._savedview)

    @property  # getter for sessiontitle State attribute
    def projectiontype(self):  # new getter property for every variable that is observed
        return self._projectiontype

    @projectiontype.setter  # setter for sessiontitle State attribute
    def projectiontype(self, data):
        self._projectiontype = data
        for callback in self._observers_projectiontype:
            callback(self._projectiontype)

    @property  # getter for sessiontitle State attribute
    def view(self):  # new getter property for every variable that is observed
        return self._view

    @view.setter  # setter for sessiontitle State attribute
    def view(self, data):
        self._view = data
        for callback in self._observers_view:
            callback(self._view)

    @property  # getter for sessiontitle State attribute
    def clippingregion(self):  # new getter property for every variable that is observed
        return self._clippingregion

    @clippingregion.setter  # setter for sessiontitle State attribute
    def clippingregion(self, data):
        self._clippingregion = data
        for callback in self._observers_clippingregion:
            callback(self._clippingregion)

    def bind_to_lightinfo(self, callback):  # Bind property to Template method
        self._observers_lightinfo.append(callback)

    def bind_to_rotationangle(self, callback):  # Bind property to Template method
        self._observers_rotationangle.append(callback)

    def bind_to_savedview(self, callback):  # Bind property to Template method
        self._observers_savedview.append(callback)

    def bind_to_projectiontype(self, callback):  # Bind property to Template method
        self._observers_projectiontype.append(callback)

    def bind_to_view(self, callback):  # Bind property to Template method
        self._observers_view.append(callback)

    def bind_to_clippingregion(self, callback):  # Bind property to Template method
        self._observers_clippingregion.append(callback)


class Graphic(object):

    def __init__(self, data, **kwargs):
        self.data = data
        self.data.bind_to_lightinfo(self.modify_lightinfo)
        self.data.bind_to_rotationangle(self.modify_rotationangle)
        self.data.bind_to_savedview(self.modify_savedview)
        self.data.bind_to_projectiontype(self.modify_projectiontype)
        self.data.bind_to_view(self.modify_view)
        self.data.bind_to_clippingregion(self.modify_clippingregion)

        self.lightinfo = self.data._lightinfo
        self.rotationangle = self.data._rotationangle
        self.savedview = self.data._savedview
        self.projectiontype = self.data._projectiontype
        self.view = self.data._view
        self.clippingregion = self.data._clippingregion

    def add_graphics(self, num_graphics, window, **kwargs):
        self.Window_i = window
        self.root = window.root
        allowed_keys = {'lightinfo', 'rotationangle', 'savedview', 'projectiontype', 'view', 'clippingregion'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

        class GraphicAttributes(object):
            Root = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None)]
            LightInfo = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            RotationAngle = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            SavedView = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ProjectionType = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            View = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ClippingRegion = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]

        Graphic = [GraphicAttributes() for i in range(num_graphics)]

        for i in range(num_graphics):  # add all pages
            graphic_i = str(i)

            type = 'graphic'
            name = type + graphic_i
            Graphic[i].Root = AnyNode(id=name, type=type, parent=self.Window_i,
                                      level=None, graphic_num=graphic_i)
            Graphic[i].Root.level = len(Graphic[i].Root.ancestors) - 1
            Graphic[i].Root.N = len(self.root.leaves)

            type = 'lightinfo'
            name = type + graphic_i
            Graphic[i].LightInfo = AnyNode(id=name, type=type, oc=1, parent=Graphic[i].Root,
                                           level=None, graphic_num=graphic_i, N=None, data=self.lightinfo)
            Graphic[i].LightInfo.level = len(Graphic[i].Root.ancestors)
            Graphic[i].LightInfo.N = len(self.root.leaves)

            type = 'rotationangle'
            name = type + graphic_i
            Graphic[i].RotationAngle = AnyNode(id=name, type=type, oc=1, parent=Graphic[i].Root,
                                               level=None, graphic_num=graphic_i, N=None, data=self.rotationangle)
            Graphic[i].RotationAngle.level = len(Graphic[i].Root.ancestors)
            Graphic[i].RotationAngle.N = len(self.root.leaves)

            type = 'savedview'
            name = type + graphic_i
            Graphic[i].SavedView = AnyNode(id=name, type=type, oc=1, parent=Graphic[i].Root,
                                               level=None, graphic_num=graphic_i, N=None, data=self.savedview)
            Graphic[i].SavedView.level = len(Graphic[i].Root.ancestors)
            Graphic[i].SavedView.N = len(self.root.leaves)

            type = 'projectiontype'
            name = type + graphic_i
            Graphic[i].ProjectionType = AnyNode(id=name, type=type, oc=1, parent=Graphic[i].SavedView,
                                           level=None, graphic_num=graphic_i, N=None, data=self.projectiontype)
            Graphic[i].ProjectionType.level = len(Graphic[i].SavedView.ancestors)
            Graphic[i].ProjectionType.N = len(self.root.leaves)

            type = 'view'
            name = type + graphic_i
            Graphic[i].View = AnyNode(id=name, type=type, oc=1, parent=Graphic[i].SavedView,
                                           level=None, graphic_num=graphic_i, N=None, data=self.view)
            Graphic[i].View.level = len(Graphic[i].SavedView.ancestors)
            Graphic[i].View.N = len(self.root.leaves)

            type = 'clippingregion'
            name = type + graphic_i
            Graphic[i].ClippingRegion = AnyNode(id=name, type=type, oc=1, parent=Graphic[i].SavedView,
                                      level=None, graphic_num=graphic_i, N=None, data=self.clippingregion)
            Graphic[i].ClippingRegion.level = len(Graphic[i].SavedView.ancestors)
            Graphic[i].ClippingRegion.N = len(self.root.leaves)

        return Graphic

    def modify_lightinfo(self, graphic_mod):
        _global_callback('lightinfo', graphic_mod)

    def modify_rotationangle(self, graphic_mod):
        _global_callback('rotationangle', graphic_mod)

    def modify_savedview(self, graphic_mod):
        _global_callback('savedview', graphic_mod)

    def modify_projectiontype(self, graphic_mod):
        _global_callback('projectiontype', graphic_mod)

    def modify_view(self, graphic_mod):
        _global_callback('view', graphic_mod)

    def modify_clippingregion(self, graphic_mod):
        _global_callback('clippingregion', graphic_mod)


class ModelState(object):

    def __init__(self, **kwargs):
        self._colorby = 'Part'
        self._color = '255 0  0'
        self._graphic = '0'
        self._deformed = ''
        self._scalemode = 'ScaleFactor'
        self._scale = '1.000000 1.000000 1.000000'
        self._resolvedinsystem = '0'
        self._resulttype = 'Displacement'

        self._observers_colorby = []
        self._observers_color = []
        self._observers_graphic = []
        self._observers_deformed = []
        self._observers_scalemode = []
        self._observers_scale = []
        self._observers_resolvedinsystem = []
        self._observers_resulttype = []

    @property  # getter for sessiontitle State attribute
    def colorby(self):  # new getter property for every variable that is observed
        return self._colorby

    @colorby.setter  # setter for sessiontitle State attribute
    def colorby(self, data):
        self._colorby = data
        for callback in self._observers_colorby:
            callback(self._colorby)

    @property  # getter for sessiontitle State attribute
    def color(self):  # new getter property for every variable that is observed
        return self._color

    @color.setter  # setter for sessiontitle State attribute
    def color(self, data):
        self._color = data
        for callback in self._observers_color:
            callback(self._color)

    @property  # getter for sessiontitle State attribute
    def graphic(self):  # new getter property for every variable that is observed
        return self._graphic

    @graphic.setter  # setter for sessiontitle State attribute
    def graphic(self, data):
        self._graphic = data
        for callback in self._observers_graphic:
            callback(self._graphic)

    @property  # getter for sessiontitle State attribute
    def deformed(self):  # new getter property for every variable that is observed
        return self._deformed

    @deformed.setter  # setter for sessiontitle State attribute
    def deformed(self, data):
        self._deformed = data
        for callback in self._observers_deformed:
            callback(self._deformed)

    @property  # getter for sessiontitle State attribute
    def scalemode(self):  # new getter property for every variable that is observed
        return self._scalemode

    @scalemode.setter  # setter for sessiontitle State attribute
    def scalemode(self, data):
        self._scalemode = data
        for callback in self._observers_scalemode:
            callback(self._scalemode)

    @property  # getter for sessiontitle State attribute
    def scale(self):  # new getter property for every variable that is observed
        return self._scale

    @scale.setter  # setter for sessiontitle State attribute
    def scale(self, data):
        self._scale = data
        for callback in self._observers_scale:
            callback(self._scale)

    @property  # getter for sessiontitle State attribute
    def resolvedinsystem(self):  # new getter property for every variable that is observed
        return self._resolvedinsystem

    @resolvedinsystem.setter  # setter for sessiontitle State attribute
    def resolvedinsystem(self, data):
        self._resolvedinsystem = data
        for callback in self._observers_resolvedinsystem:
            callback(self._resolvedinsystem)

    @property  # getter for sessiontitle State attribute
    def resulttype(self):  # new getter property for every variable that is observed
        return self._resulttype

    @resulttype.setter  # setter for sessiontitle State attribute
    def resulttype(self, data):
        self._resulttype = data
        for callback in self._observers_resulttype:
            callback(self._resulttype)

    def bind_to_colorby(self, callback):  # Bind property to Template method
        self._observers_colorby.append(callback)

    def bind_to_color(self, callback):  # Bind property to Template method
        self._observers_color.append(callback)

    def bind_to_graphic(self, callback):  # Bind property to Template method
        self._observers_graphic.append(callback)
    
    def bind_to_deformed(self, callback):  # Bind property to Template method
        self._observers_deformed.append(callback)
    
    def bind_to_scalemode(self, callback):  # Bind property to Template method
        self._observers_scalemode.append(callback)
    
    def bind_to_scale(self, callback):  # Bind property to Template method
        self._observers_scale.append(callback)
    
    def bind_to_resolvedinsystem(self, callback):  # Bind property to Template method
        self._observers_resolvedinsystem.append(callback)
    
    def bind_to_resulttype(self, callback):  # Bind property to Template method
        self._observers_resulttype.append(callback)


class Model(object):

    def __init__(self, data, **kwargs):
        self.data = data
        self.data.bind_to_colorby(self.modify_colorby)
        self.data.bind_to_color(self.modify_color)
        self.data.bind_to_graphic(self.modify_graphic)
        self.data.bind_to_deformed(self.modify_deformed)
        self.data.bind_to_scalemode(self.modify_scalemode)
        self.data.bind_to_scale(self.modify_scale)
        self.data.bind_to_resolvedinsystem(self.modify_resolvedinsystem)
        self.data.bind_to_resulttype(self.modify_resulttype)

        self.colorby = self.data._colorby
        self.color = self.data._color
        self.graphic = self.data._graphic
        self.deformed = self.data._deformed
        self.scalemode = self.data._scalemode
        self.scale = self.data._scale
        self.resolvedinsystem = self.data._resolvedinsystem
        self.resulttype = self.data._resulttype

    def add_model(self, num_models, graphic, **kwargs):
        self.Graphic_i = graphic
        self.root = graphic.root
        allowed_keys = {'color', 'colorby', 'scalemode', 'scale', 'resolvedinsystem', 'resulttype'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

        class ModelAttributes(object):
            Root = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ColorBy = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Color = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Deformed = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ScaleMode = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Scale = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ResolvedInSystem = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ResultType = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]

        Model = [ModelAttributes() for i in range(num_models)]

        for i in range(num_models):  # add all pages
            model_i = str(i)

            type = 'model'
            name = type + model_i
            Model[i].Root = AnyNode(id=name, type=type, parent=self.Graphic_i,
                                    level=None, model_num=model_i, data=self.graphic)
            Model[i].Root.level = len(Model[i].Root.ancestors) - 1
            Model[i].Root.N = len(self.root.leaves)

            type = 'colorby'
            name = type + model_i
            Model[i].ColorBy = AnyNode(id=name, type=type, oc=1, parent=Model[i].Root,
                                       level=None, model_num=model_i, N=None, data=self.colorby)
            Model[i].ColorBy.level = len(Model[i].Root.ancestors)
            Model[i].ColorBy.N = len(self.root.leaves)

            type = 'color'
            name = type + model_i
            Model[i].Color = AnyNode(id=name, type=type, oc=1, parent=Model[i].Root,
                                     level=None, model_num=model_i, N=None, data=self.color)
            Model[i].Color.level = len(Model[i].Root.ancestors)
            Model[i].Color.N = len(self.root.leaves)

            type = 'deformed'
            name = type + model_i
            Model[i].Deformed = AnyNode(id=name, type=type, oc=1, parent=Model[i].Root,
                                     level=None, model_num=model_i, N=None, data=self.deformed)
            Model[i].Deformed.level = len(Model[i].Root.ancestors)
            Model[i].Deformed.N = len(self.root.leaves)

            type = 'scalemode'
            name = type + model_i
            Model[i].ScaleMode = AnyNode(id=name, type=type, oc=1, parent=Model[i].Deformed,
                                        level=None, model_num=model_i, N=None, data=self.scalemode)
            Model[i].ScaleMode.level = len(Model[i].Deformed.ancestors)
            Model[i].ScaleMode.N = len(self.root.leaves)

            type = 'scale'
            name = type + model_i
            Model[i].Scale = AnyNode(id=name, type=type, oc=1, parent=Model[i].Deformed,
                                         level=None, model_num=model_i, N=None, data=self.scale)
            Model[i].Scale.level = len(Model[i].Deformed.ancestors)
            Model[i].Scale.N = len(self.root.leaves)

            type = 'resolvedinsystem'
            name = type + model_i
            Model[i].ResolvedInSystem = AnyNode(id=name, type=type, oc=1, parent=Model[i].Deformed,
                                     level=None, model_num=model_i, N=None, data=self.resolvedinsystem)
            Model[i].ResolvedInSystem.level = len(Model[i].Deformed.ancestors)
            Model[i].ResolvedInSystem.N = len(self.root.leaves)

            type = 'resulttype'
            name = type + model_i
            Model[i].ResultType= AnyNode(id=name, type=type, oc=1, parent=Model[i].Deformed,
                                                level=None, model_num=model_i, N=None, data=self.resulttype)
            Model[i].ResultType.level = len(Model[i].Deformed.ancestors)
            Model[i].ResultType.N = len(self.root.leaves)

        return Model

    def modify_graphic(self, model_mod):
        _global_callback('graphic', model_mod)

    def modify_colorby(self, model_mod):
        _global_callback('colorby', model_mod)

    def modify_color(self, model_mod):
        _global_callback('color', model_mod)
    
    def modify_deformed(self, model_mod):
        _global_callback('deformed', model_mod)
    
    def modify_scalemode(self, model_mod):
        _global_callback('scalemode', model_mod)
    
    def modify_scale(self, model_mod):
        _global_callback('scale', model_mod)
        
    def modify_resolvedinsystem(self, model_mod):
        _global_callback('resolvedinsystem', model_mod)
    
    def modify_resulttype(self, model_mod):
        _global_callback('resulttype', model_mod)


class ResultState(object):

    def __init__(self, **kwargs):
        self._result = '0'
        self._currentsubcase = '1, 0'

        self._observers_result = []
        self._observers_currentsubcase = []

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, data):
        self._result = data
        for callback in self._observers_result:
            callback(self._result)

    @property
    def currentsubcase(self):
        return self._currentsubcase

    @currentsubcase.setter
    def currentsubcase(self, data):
        self._currentsubcase = data
        for callback in self._observers_currentsubcase:
            callback(self._currentsubcase)

    def bind_to_result(self, callback):
        self._observers_result.append(callback)

    def bind_to_currentsubcase(self, callback):
        self._observers_currentsubcase.append(callback)


class Result(object):

    def __init__(self, data, **kwargs):
        self.data = data
        self.data.bind_to_result(self.modify_result)
        self.data.bind_to_currentsubcase(self.modify_currentsubcase)

        self.result = self.data._result
        self.currentsubcase = self.data._currentsubcase

    def add_result(self, num_results, model, **kwargs):
        self.Model_i = model
        self.root = model.root
        allowed_keys = {'currentsubcase'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

        class ResultAttributes(object):
            Root = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            CurrentSubcase = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]

        Result = [ResultAttributes() for i in range(num_results)]

        for i in range(num_results):  # add all pages
            result_i = str(i)

            type = 'result'
            name = type + result_i
            Result[i].Root = AnyNode(id=name, type=type, parent=self.Model_i,
                                     level=None, result_num=result_i, data=self.result)
            Result[i].Root.level = len(Result[i].Root.ancestors) - 1
            Result[i].Root.N = len(self.root.leaves)

            type = 'currentsubcase'
            name = type + result_i
            Result[i].CurrentSubcase = AnyNode(id=name, type=type, oc=1, parent=Result[i].Root,
                                               level=None, result_num=result_i, N=None, data=self.currentsubcase)
            Result[i].CurrentSubcase.level = len(Result[i].Root.ancestors)
            Result[i].CurrentSubcase.N = len(self.root.leaves)

        return Result

    def modify_result(self, result_mod):
        _global_callback('result', result_mod)

    def modify_currentsubcase(self, result_mod):
        _global_callback('currentsubcase', result_mod)


class PartState(object):

    def __init__(self, **kwargs):
        self._part = ', "Global", "PART", 0'
        self._attribute = 'On, IdOff, 6, Opa, Sha, Msh, InFit, InCut, InIso'

        self._observers_part = []
        self._observers_attribute = []

    @property
    def part(self):
        return self._part

    @part.setter
    def part(self, data):
        self._part = data
        for callback in self._observers_part:
            callback(self._part)

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, data):
        self._attribute = data
        for callback in self._observers_attribute:
            callback(self._attribute)

    def bind_to_part(self, callback):
        self._observers_part.append(callback)

    def bind_to_attribute(self, callback):
        self._observers_attribute.append(callback)


class Part(object):

    def __init__(self, data, **kwargs):
        self.data = data
        self.data.bind_to_part(self.modify_part)
        self.data.bind_to_attribute(self.modify_attribute)

        self.part = self.data._part
        self.attribute = self.data._attribute

    def add_part(self, num_parts, model, **kwargs):
        self.Model_i = model
        self.root = model.root
        allowed_keys = {'attribute'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

        class PartAttributes(object):
            Root = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Attribute = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]

        Part = [PartAttributes() for i in range(num_parts)]

        for i in range(num_parts):  # add all pages
            part_i = str(i)

            type = 'part'
            name = type + part_i
            Part[i].Root = AnyNode(id=name, type=type, parent=self.Model_i,
                                   level=None, part_num=part_i, data=str(int(part_i) + 1) + self.part)
            Part[i].Root.level = len(Part[i].Root.ancestors) - 1
            Part[i].Root.N = len(self.root.leaves)

            type = 'attribute'
            name = type + part_i
            Part[i].Attribute = AnyNode(id=name, type=type, oc=1, parent=Part[i].Root,
                                        level=None, part_num=part_i, N=None, data=self.attribute)
            Part[i].Attribute.level = len(Part[i].Root.ancestors)
            Part[i].Attribute.N = len(self.root.leaves)

        return Part

    def modify_part(self, part_mod):
        _global_callback('part', part_mod)

    def modify_attribute(self, part_mod):
        _global_callback('attribute', part_mod)


class GroupState(object):

    def __init__(self, **kwargs):
        self._group = 'D Set", "Off", "Off", "  0   0 255", 1, "wire"'
        self._selection = 'Part, SelectAll, "User_Set", '

        self._observers_group = []
        self._observers_selection = []

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, data):
        self._group = data
        for callback in self._observers_group:
            callback(self._group)

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, data):
        self._selection = data
        for callback in self._observers_selection:
            callback(self._selection)

    def bind_to_group(self, callback):
        self._observers_group.append(callback)

    def bind_to_selection(self, callback):
        self._observers_selection.append(callback)


class Group(object):

    def __init__(self, data, **kwargs):
        self.data = data
        self.data.bind_to_group(self.modify_group)
        self.data.bind_to_selection(self.modify_selection)

        self.group = self.data._group
        self.selection = self.data._selection

    def add_group(self, num_groups, dimension, model, **kwargs):
        self.Model_i = model
        self.root = model.root
        allowed_keys = {'selection'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

        class GroupAttributes(object):
            Root = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Selection = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Add = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]

        Group = [GroupAttributes() for i in range(num_groups)]

        for i in range(num_groups):  # add all pages
            group_i = str(i)

            type = 'group'
            name = type + group_i
            Group[i].Root = AnyNode(id=name, type=type, parent=self.Model_i,
                                   level=None, group_num=group_i, data='"'+str(dimension) + self.group)
            Group[i].Root.level = len(Group[i].Root.ancestors) - 1
            Group[i].Root.N = len(self.root.leaves)

            type = 'groupselection'
            name = type + group_i
            Group[i].Selection = AnyNode(id=name, type=type, oc=1, parent=Group[i].Root,
                                        level=None, group_num=group_i, N=None, data=self.selection + str(i+1))
            Group[i].Selection.level = len(Group[i].Root.ancestors)
            Group[i].Selection.N = len(self.root.leaves)

            type = 'groupselectionadd'
            name = type + group_i
            Group[i].Add = AnyNode(id=name, type=type, oc=1, parent=Group[i].Selection,
                                         level=None, group_num=group_i, N=None, data='dimension == ' + str(dimension))
            Group[i].Add.level = len(Group[i].Selection.ancestors)
            Group[i].Add.N = len(self.root.leaves)

        return Group

    def modify_group(self, group_mod):
        _global_callback('group', group_mod)

    def modify_selection(self, group_mod):
        _global_callback('selection', group_mod)


class ContourState(object):

    def __init__(self, **kwargs):
        self._contour = ''
        self._selection = 'Part, SelectAll, "User_Set", '
        self._add = 'Displayed'
        self._resulttype = 'Displacement'
        self._displayoptions = '"ContourOn", "LegendOn", "MeasuresOn", "NotesOn"'
        self._datacomponent = 'Mag'
        self._multiplelayers = 'false'
        self._layer = 'Max'
        self._layerfilter = '0'
        self._complexfilter = 'mag'
        self._resolvedinsystem = '-1'
        self._averagingmethod = '"Simple", -0.01'
        self._averageacrossparts = 'Off'
        self._showmidsidenoderesults = 'On'
        self._featureangleaverage = 'Off, 50, On'
        self._averagecolor = 'yes'
        self._discretecolor = 'yes'

        self._observers_contour = []
        self._observers_selection = []
        self._observers_add = []
        self._observers_resulttype = []
        self._observers_displayoptions = []
        self._observers_datacomponent = []
        self._observers_multiplelayers = []
        self._observers_layer = []
        self._observers_layerfilter = []
        self._observers_complexfilter = []
        self._observers_resolvedinsystem = []
        self._observers_averagingmethod = []
        self._observers_averageacrossparts = []
        self._observers_showmidsidenoderesults = []
        self._observers_featureangleaverage = []
        self._observers_averagecolor = []
        self._observers_discretecolor = []

    @property
    def contour(self):
        return self._contour

    @contour.setter
    def contour(self, data):
        self._contour = data
        for callback in self._observers_contour:
            callback(self._contour)

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, data):
        self._selection = data
        for callback in self._observers_selection:
            callback(self._selection)

    @property
    def add(self):
        return self._add

    @add.setter
    def add(self, data):
        self._add = data
        for callback in self._observers_add:
            callback(self._add)

    @property
    def resulttype(self):
        return self._resulttype

    @resulttype.setter
    def resulttype(self, data):
        self._resulttype = data
        for callback in self._observers_resulttype:
            callback(self._resulttype)

    @property
    def displayoptions(self):
        return self._displayoptions

    @displayoptions.setter
    def displayoptions(self, data):
        self._displayoptions = data
        for callback in self._observers_displayoptions:
            callback(self._displayoptions)

    @property
    def datacomponent(self):
        return self._datacomponent

    @datacomponent.setter
    def datacomponent(self, data):
        self._datacomponent = data
        for callback in self._observers_datacomponent:
            callback(self._datacomponent)

    @property
    def multiplelayers(self):
        return self._multiplelayers

    @multiplelayers.setter
    def multiplelayers(self, data):
        self._multiplelayers = data
        for callback in self._observers_multiplelayers:
            callback(self._multiplelayers)

    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, data):
        self._layer = data
        for callback in self._observers_layer:
            callback(self._layer)

    @property
    def layerfilter(self):
        return self._layerfilter

    @layerfilter.setter
    def layerfilter(self, data):
        self._layerfilter = data
        for callback in self._observers_layerfilter:
            callback(self._layerfilter)

    @property
    def complexfilter(self):
        return self._complexfilter

    @complexfilter.setter
    def complexfilter(self, data):
        self._complexfilter = data
        for callback in self._observers_complexfilter:
            callback(self._complexfilter)

    @property
    def resolvedinsystem(self):
        return self._resolvedinsystem

    @resolvedinsystem.setter
    def resolvedinsystem(self, data):
        self._resolvedinsystem = data
        for callback in self._observers_resolvedinsystem:
            callback(self._resolvedinsystem)

    @property
    def averagingmethod(self):
        return self._averagingmethod

    @averagingmethod.setter
    def averagingmethod(self, data):
        self._averagingmethod = data
        for callback in self._observers_averagingmethod:
            callback(self._averagingmethod)

    @property
    def averageacrossparts(self):
        return self._averageacrossparts

    @averageacrossparts.setter
    def averageacrossparts(self, data):
        self._averageacrossparts = data
        for callback in self._observers_averageacrossparts:
            callback(self._averageacrossparts)

    @property
    def showmidsidenoderesults(self):
        return self._showmidsidenoderesults

    @showmidsidenoderesults.setter
    def showmidsidenoderesults(self, data):
        self._showmidsidenoderesults = data
        for callback in self._observers_showmidsidenoderesults:
            callback(self._showmidsidenoderesults)

    @property
    def featureangleaverage(self):
        return self._featureangleaverage

    @featureangleaverage.setter
    def featureangleaverage(self, data):
        self._featureangleaverage = data
        for callback in self._observers_featureangleaverage:
            callback(self._featureangleaverage)

    @property
    def averagecolor(self):
        return self._averagecolor

    @averagecolor.setter
    def averagecolor(self, data):
        self._averagecolor = data
        for callback in self._observers_averagecolor:
            callback(self._averagecolor)
    
    @property
    def discretecolor(self):
        return self._discretecolor

    @discretecolor.setter
    def discretecolor(self, data):
        self._discretecolor = data
        for callback in self._observers_discretecolor:
            callback(self._discretecolor)

    def bind_to_contour(self, callback):
        self._observers_contour.append(callback)

    def bind_to_selection(self, callback):
        self._observers_selection.append(callback)

    def bind_to_add(self, callback):
        self._observers_add.append(callback)

    def bind_to_resulttype(self, callback):
        self._observers_resulttype.append(callback)

    def bind_to_displayoptions(self, callback):
        self._observers_displayoptions.append(callback)

    def bind_to_datacomponent(self, callback):
        self._observers_datacomponent.append(callback)

    def bind_to_multiplelayers(self, callback):
        self._observers_multiplelayers.append(callback)

    def bind_to_layer(self, callback):
        self._observers_layer.append(callback)

    def bind_to_layerfilter(self, callback):
        self._observers_layerfilter.append(callback)

    def bind_to_complexfilter(self, callback):
        self._observers_complexfilter.append(callback)

    def bind_to_resolvedinsystem(self, callback):
        self._observers_resolvedinsystem.append(callback)

    def bind_to_averagingmethod(self, callback):
        self._observers_averagingmethod.append(callback)

    def bind_to_averageacrossparts(self, callback):
        self._observers_averageacrossparts.append(callback)
    
    def bind_to_showmidsidenoderesults(self, callback):
        self._observers_showmidsidenoderesults.append(callback)
    
    def bind_to_featureangleaverage(self, callback):
        self._observers_featureangleaverage.append(callback)
        
    def bind_to_averagecolor(self, callback):
        self._observers_averagecolor.append(callback)
    
    def bind_to_discretecolor(self, callback):
        self._observers_discretecolor.append(callback)


class Contour(object):

    def __init__(self, data, **kwargs):
        self.data = data
        self.data.bind_to_contour(self.modify_contour)
        self.data.bind_to_selection(self.modify_selection)
        self.data.bind_to_add(self.modify_add)
        self.data.bind_to_resulttype(self.modify_resulttype)
        self.data.bind_to_displayoptions(self.modify_displayoptions)
        self.data.bind_to_datacomponent(self.modify_datacomponent)
        self.data.bind_to_multiplelayers(self.modify_multiplelayers)
        self.data.bind_to_layer(self.modify_layer)
        self.data.bind_to_layerfilter(self.modify_layerfilter)
        self.data.bind_to_complexfilter(self.modify_complexfilter)
        self.data.bind_to_resolvedinsystem(self.modify_resolvedinsystem)
        self.data.bind_to_averagingmethod(self.modify_averagingmethod)
        self.data.bind_to_averageacrossparts(self.modify_averageacrossparts)
        self.data.bind_to_showmidsidenoderesults(self.modify_showmidsidenoderesults)
        self.data.bind_to_featureangleaverage(self.modify_featureangleaverage)
        self.data.bind_to_averagecolor(self.modify_averagecolor)
        self.data.bind_to_discretecolor(self.modify_discretecolor)

        self.contour = self.data._contour
        self.selection = self.data._selection
        self.add = self.data._add
        self.resulttype = self.data._resulttype
        self.displayoptions = self.data._displayoptions
        self.datacomponent = self.data._datacomponent
        self.multiplelayers = self.data._multiplelayers
        self.layer = self.data._layer
        self.layerfilter = self.data._layerfilter
        self.complexfilter = self.data._complexfilter
        self.resolvedinsystem = self.data._resolvedinsystem
        self.averagingmethod = self.data._averagingmethod
        self.averageacrossparts = self.data._averageacrossparts
        self.showmidsidenoderesults = self.data._showmidsidenoderesults
        self.featureangleaverage = self.data._featureangleaverage
        self.averagecolor = self.data._averagecolor
        self.discretecolor = self.data._discretecolor

    def add_contour(self, num_contours, model, **kwargs):
        self.Model_i = model
        self.Graphic_i = _get_parent(model, 'Graphic')
        self.root = model.root
        allowed_keys = {'selection', 'resulttype', 'displayoptions', 'datacomponent', 'layer', 'layerfilter',
                        'complexfilter', 'resolvedinsystem', 'averagingsystem', 'averagingmethod', 'averageacrossparts',
                        'showmidsidenoderesults', 'featureangleaverage', 'averagecolor', 'discretecolor'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

        class ContourAttributes(object):
            Root = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Selection = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Add = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ResultType = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            DisplayOptions = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            DataComponent = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            MultipleLayers = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Layer = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            LayerFilter = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ComplexFilter = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ResolvedInSystem = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            AveragingMethod = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            AverageAcrossParts = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ShowMidsideNodeResults = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            FeatureAngleAverage = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            AverageColor = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            DiscreteColor = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]

        Contour = [ContourAttributes() for i in range(num_contours)]

        if _is_valid_contour(self.resulttype, self.datacomponent):
            for i in range(num_contours):  # add all pages
                contour_i = str(i)

                type = 'contour'
                name = type + contour_i
                Contour[i].Root = AnyNode(id=name, type=type, parent=self.Model_i,
                                        level=None, contour_num=contour_i, data='')
                Contour[i].Root.level = len(Contour[i].Root.ancestors) - 1
                Contour[i].Root.N = len(self.root.leaves)

                type = 'contourselection'
                name = type + contour_i
                Contour[i].Selection = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                             level=None, contour_num=contour_i, N=None, data=self.selection + str(i + 1))
                Contour[i].Selection.level = len(Contour[i].Root.ancestors)
                Contour[i].Selection.N = len(self.root.leaves)

                type = 'contourselectionadd'
                name = type + contour_i
                Contour[i].Add = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Selection,
                                       level=None, contour_num=contour_i, N=None, data=self.add)
                Contour[i].Add.level = len(Contour[i].Selection.ancestors)
                Contour[i].Add.N = len(self.root.leaves)

                type = 'resulttype'
                name = type + contour_i
                Contour[i].ResultType = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                         level=None, contour_num=contour_i, N=None, data=self.resulttype)
                Contour[i].ResultType.level = len(Contour[i].Root.ancestors)
                Contour[i].ResultType.N = len(self.root.leaves)

                type = 'displayoptions'
                name = type + contour_i
                Contour[i].DisplayOptions = AnyNode(id=name, type=type, oc=1, parent=self.Graphic_i,
                                                level=None, contour_num=contour_i, N=None, data=self.displayoptions)
                Contour[i].DisplayOptions.level = len(self.Graphic_i.ancestors)
                Contour[i].DisplayOptions.N = len(self.root.leaves)

                type = 'datacomponent'
                name = type + contour_i
                Contour[i].DataComponent = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                                    level=None, contour_num=contour_i, N=None, data=self.datacomponent)
                Contour[i].DataComponent.level = len(Contour[i].Root.ancestors)
                Contour[i].DataComponent.N = len(self.root.leaves)

                type = 'multiplelayers'
                name = type + contour_i
                Contour[i].MultipleLayers = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                                   level=None, contour_num=contour_i, N=None, data=self.multiplelayers)
                Contour[i].MultipleLayers.level = len(Contour[i].Root.ancestors)
                Contour[i].MultipleLayers.N = len(self.root.leaves)

                type = 'layer'
                name = type + contour_i
                Contour[i].Layer = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                                    level=None, contour_num=contour_i, N=None,
                                                    data=self.layer)
                Contour[i].Layer.level = len(Contour[i].Root.ancestors)
                Contour[i].Layer.N = len(self.root.leaves)

                type = 'layerfilter'
                name = type + contour_i
                Contour[i].LayerFilter = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                           level=None, contour_num=contour_i, N=None,
                                           data=self.layerfilter)
                Contour[i].LayerFilter.level = len(Contour[i].Root.ancestors)
                Contour[i].LayerFilter.N = len(self.root.leaves)

                type = 'complexfilter'
                name = type + contour_i
                Contour[i].ComplexFilter = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                                 level=None, contour_num=contour_i, N=None,
                                                 data=self.complexfilter)
                Contour[i].ComplexFilter.level = len(Contour[i].Root.ancestors)
                Contour[i].ComplexFilter.N = len(self.root.leaves)

                type = 'resolvedinsystem'
                name = type + contour_i
                Contour[i].ResolvedInSystem = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                                   level=None, contour_num=contour_i, N=None,
                                                   data=self.resolvedinsystem)
                Contour[i].ResolvedInSystem.level = len(Contour[i].Root.ancestors)
                Contour[i].ResolvedInSystem.N = len(self.root.leaves)

                type = 'averagingmethod'
                name = type + contour_i
                Contour[i].AveragingMethod = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                                      level=None, contour_num=contour_i, N=None,
                                                      data=self.averagingmethod)
                Contour[i].AveragingMethod.level = len(Contour[i].Root.ancestors)
                Contour[i].AveragingMethod.N = len(self.root.leaves)

                type = 'averageacrossparts'
                name = type + contour_i
                Contour[i].AverageAcrossParts = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                                     level=None, contour_num=contour_i, N=None,
                                                     data =self.averageacrossparts)
                Contour[i].AverageAcrossParts.level = len(Contour[i].Root.ancestors)
                Contour[i].AverageAcrossParts.N = len(self.root.leaves)

                type = 'showmidsidenoderesults'
                name = type + contour_i
                Contour[i].ShowMidsideNodeResults = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                                        level=None, contour_num=contour_i, N=None,
                                                        data=self.showmidsidenoderesults)
                Contour[i].ShowMidsideNodeResults.level = len(Contour[i].Root.ancestors)
                Contour[i].ShowMidsideNodeResults.N = len(self.root.leaves)

                type = 'featureangleaverage'
                name = type + contour_i
                Contour[i].FeatureAngleAverage = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                                            level=None, contour_num=contour_i, N=None,
                                                            data=self.featureangleaverage)
                Contour[i].FeatureAngleAverage.level = len(Contour[i].Root.ancestors)
                Contour[i].FeatureAngleAverage.N = len(self.root.leaves)

                type = 'averagecolor'
                name = type + contour_i
                Contour[i].AverageColor = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                                   level=None, contour_num=contour_i, N=None,
                                                   data=self.averagecolor)
                Contour[i].AverageColor.level = len(Contour[i].Root.ancestors)
                Contour[i].AverageColor.N = len(self.root.leaves)
                
                type = 'discretecolor'
                name = type + contour_i
                Contour[i].DiscreteColor = AnyNode(id=name, type=type, oc=1, parent=Contour[i].Root,
                                                            level=None, contour_num=contour_i, N=None,
                                                            data=self.discretecolor)
                Contour[i].DiscreteColor.level = len(Contour[i].Root.ancestors)
                Contour[i].DiscreteColor.N = len(self.root.leaves)

        else:
            print('\n :: Error :: Invalid contour specified.\n')
            quit()

        return Contour

    def modify_contour(self, contour_mod):
        _global_callback('contour', contour_mod)

    def modify_selection(self, contour_mod):
        _global_callback('selection', contour_mod)

    def modify_add(self, contour_mod):
        _global_callback('add', contour_mod)

    def modify_resulttype(self, contour_mod):
        _global_callback('resulttype', contour_mod)

    def modify_displayoptions(self, contour_mod):
        _global_callback('displayoptions', contour_mod)

    def modify_datacomponent(self, contour_mod):
        _global_callback('datacomponent', contour_mod)

    def modify_multiplelayers(self, contour_mod):
        _global_callback('multiplelayers', contour_mod)

    def modify_layer(self, contour_mod):
        _global_callback('layer', contour_mod)

    def modify_layerfilter(self, contour_mod):
        _global_callback('layerfilter', contour_mod)

    def modify_complexfilter(self, contour_mod):
        _global_callback('complexfilter', contour_mod)

    def modify_resolvedinsystem(self, contour_mod):
        _global_callback('resolvedinsystem', contour_mod)

    def modify_averagingmethod(self, contour_mod):
        _global_callback('averagingmethod', contour_mod)

    def modify_averageacrossparts(self, contour_mod):
        _global_callback('averageacrossparts', contour_mod)
    
    def modify_showmidsidenoderesults(self, contour_mod):
        _global_callback('showmidsidenoderesults', contour_mod)

    def modify_featureangleaverage(self, contour_mod):
        _global_callback('featureangleaverage', contour_mod)

    def modify_averagecolor(self, contour_mod):
        _global_callback('averagecolor', contour_mod)

    def modify_discretecolor(self, contour_mod):
        _global_callback('discretecolor', contour_mod)


class LegendState(object):

    def __init__(self, **kwargs):
        self._legend = ''
        self._legendtype = 'Static'
        self._numcols = '9'
        self._legendmaxthreshold = '"Off", 1'
        self._legendminthreshold = 'Off, 0'
        self._colorrgb = '"0 0 200", "21 121 255", "0 199 221", "40 255 185", "57 255 0", ' \
                         '"170 255 0", "255 227 0", "255 113 0", "255 0 0"'
        self._noresultcolor = '192 192 192'
        self._numbers = '"show", "scientific", 3'
        self._showmax = 'show'
        self._showmaxlocal = 'hide'
        self._showmin = 'show'
        self._showminlocal = 'hide'
        self._entitylabel = 'show'
        self._showbymodel = 'hide'
        self._legendposition = 'UpperLeft'
        self._backgroundcolor = ' 44  85 126'
        self._transparency = 'On'
        self._filter = 'LINEAR'

        self._observers_legend = []
        self._observers_legendtype = []
        self._observers_numcols = []
        self._observers_legendmaxthreshold = []
        self._observers_legendminthreshold = []
        self._observers_colorrgb = []
        self._observers_noresultcolor = []
        self._observers_numbers = []
        self._observers_showmax = []
        self._observers_showmaxlocal = []
        self._observers_showmin = []
        self._observers_showminlocal = []
        self._observers_entitylabel = []
        self._observers_showbymodel = []
        self._observers_legendposition = []
        self._observers_backgroundcolor = []
        self._observers_transparency = []
        self._observers_filter = []

    @property
    def legend(self):
        return self._legend

    @legend.setter
    def legend(self, data):
        self._legend = data
        for callback in self._observers_legend:
            callback(self._legend)

    @property
    def legendtype(self):
        return self._legendtype

    @legendtype.setter
    def legendtype(self, data):
        self._legendtype = data
        for callback in self._observers_legendtype:
            callback(self._legendtype)

    @property
    def numcols(self):
        return self._numcols

    @numcols.setter
    def numcols(self, data):
        self._numcols = data
        for callback in self._observers_numcols:
            callback(self._numcols)

    @property
    def legendmaxthreshold(self):
        return self._legendmaxthreshold

    @legendmaxthreshold.setter
    def legendmaxthreshold(self, data):
        self._legendmaxthreshold = data
        for callback in self._observers_legendmaxthreshold:
            callback(self._legendmaxthreshold)

    @property
    def legendminthreshold(self):
        return self._legendminthreshold

    @legendminthreshold.setter
    def legendminthreshold(self, data):
        self._legendminthreshold = data
        for callback in self._observers_legendminthreshold:
            callback(self._legendminthreshold)

    @property
    def colorrgb(self):
        return self._colorrgb

    @colorrgb.setter
    def colorrgb(self, data):
        self._colorrgb = data
        for callback in self._observers_colorrgb:
            callback(self._colorrgb)

    @property
    def noresultcolor(self):
        return self._noresultcolor

    @noresultcolor.setter
    def noresultcolor(self, data):
        self._noresultcolor = data
        for callback in self._observers_noresultcolor:
            callback(self._noresultcolor)

    @property
    def numbers(self):
        return self._numbers

    @numbers.setter
    def numbers(self, data):
        self._numbers = data
        for callback in self._observers_numbers:
            callback(self._numbers)

    @property
    def showmax(self):
        return self._showmax

    @showmax.setter
    def showmax(self, data):
        self._showmax = data
        for callback in self._observers_showmax:
            callback(self._showmax)

    @property
    def showmaxlocal(self):
        return self._showmaxlocal

    @showmaxlocal.setter
    def showmaxlocal(self, data):
        self._showmaxlocal = data
        for callback in self._observers_showmaxlocal:
            callback(self._showmaxlocal)

    @property
    def showmin(self):
        return self._showmin

    @showmin.setter
    def showmin(self, data):
        self._showmin = data
        for callback in self._observers_showmin:
            callback(self._showmin)

    @property
    def showminlocal(self):
        return self._showminlocal

    @showminlocal.setter
    def showminlocal(self, data):
        self._showminlocal = data
        for callback in self._observers_showminlocal:
            callback(self._showminlocal)

    @property
    def entitylabel(self):
        return self._entitylabel

    @entitylabel.setter
    def entitylabel(self, data):
        self._entitylabel = data
        for callback in self._observers_entitylabel:
            callback(self._entitylabel)

    @property
    def showbymodel(self):
        return self._showbymodel

    @showbymodel.setter
    def showbymodel(self, data):
        self._showbymodel = data
        for callback in self._observers_showbymodel:
            callback(self._showbymodel)

    @property
    def legendposition(self):
        return self._legendposition

    @legendposition.setter
    def legendposition(self, data):
        self._legendposition = data
        for callback in self._observers_legendposition:
            callback(self._legendposition)

    @property
    def backgroundcolor(self):
        return self._backgroundcolor

    @backgroundcolor.setter
    def backgroundcolor(self, data):
        self._backgroundcolor = data
        for callback in self._observers_backgroundcolor:
            callback(self._backgroundcolor)

    @property
    def transparency(self):
        return self._transparency

    @transparency.setter
    def transparency(self, data):
        self._transparency = data
        for callback in self._observers_transparency:
            callback(self._transparency)

    @property
    def filter(self):
        return self._filter

    @filter.setter
    def filter(self, data):
        self._filter = data
        for callback in self._observers_filter:
            callback(self._filter)
            
    def bind_to_legend(self, callback):
        self._observers_legend.append(callback)

    def bind_to_legendtype(self, callback):
        self._observers_legendtype.append(callback)
    
    def bind_to_numcols(self, callback):
        self._observers_numcols.append(callback)
    
    def bind_to_legendmaxthreshold(self, callback):
        self._observers_legendmaxthreshold.append(callback)
    
    def bind_to_legendminthreshold(self, callback):
        self._observers_legendminthreshold.append(callback)
        
    def bind_to_colorrgb(self, callback):
        self._observers_colorrgb.append(callback)
    
    def bind_to_noresultcolor(self, callback):
        self._observers_noresultcolor.append(callback)
    
    def bind_to_numbers(self, callback):
        self._observers_numbers.append(callback)
        
    def bind_to_showmax(self, callback):
        self._observers_showmax.append(callback)
    
    def bind_to_showmaxlocal(self, callback):
        self._observers_showmaxlocal.append(callback)

    def bind_to_showmin(self, callback):
        self._observers_showmin.append(callback)

    def bind_to_showminlocal(self, callback):
        self._observers_showminlocal.append(callback)

    def bind_to_entitylabel(self, callback):
        self._observers_entitylabel.append(callback)
    
    def bind_to_showbymodel(self, callback):
        self._observers_showbymodel.append(callback)
    
    def bind_to_legendposition(self, callback):
        self._observers_legendposition.append(callback)
    
    def bind_to_backgroundcolor(self, callback):
        self._observers_backgroundcolor.append(callback)
    
    def bind_to_transparency(self, callback):
        self._observers_transparency.append(callback)
    
    def bind_to_filter(self, callback):
        self._observers_filter.append(callback)


class Legend(object):

    def __init__(self, data, **kwargs):
        self.data = data
        self.data.bind_to_legend(self.modify_legend)
        self.data.bind_to_legendtype(self.modify_legendtype)
        self.data.bind_to_numcols(self.modify_numcols)
        self.data.bind_to_legendmaxthreshold(self.modify_legendmaxthreshold)
        self.data.bind_to_legendminthreshold(self.modify_legendminthreshold)
        self.data.bind_to_colorrgb(self.modify_colorrgb)
        self.data.bind_to_noresultcolor(self.modify_noresultcolor)
        self.data.bind_to_numbers(self.modify_numbers)
        self.data.bind_to_showmax(self.modify_showmax)
        self.data.bind_to_showmaxlocal(self.modify_showmaxlocal)
        self.data.bind_to_showmin(self.modify_showmin)
        self.data.bind_to_showminlocal(self.modify_showminlocal)
        self.data.bind_to_entitylabel(self.modify_entitylabel)
        self.data.bind_to_showbymodel(self.modify_showbymodel)
        self.data.bind_to_legendposition(self.modify_legendposition)
        self.data.bind_to_backgroundcolor(self.modify_backgroundcolor)
        self.data.bind_to_transparency(self.modify_transparency)
        self.data.bind_to_filter(self.modify_filter)

        self.legend = self.data._legend
        self.legendtype = self.data._legendtype
        self.numcols = self.data._numcols
        self.legendmaxthreshold = self.data._legendmaxthreshold
        self.legendminthreshold = self.data._legendminthreshold
        self.colorrgb = self.data._colorrgb
        self.noresultcolor = self.data._noresultcolor
        self.numbers = self.data._numbers
        self.showmax = self.data._showmax
        self.showmaxlocal = self.data._showmaxlocal
        self.showmin = self.data._showmin
        self.showminlocal = self.data._showminlocal
        self.entitylabel = self.data._entitylabel
        self.showbymodel = self.data._showbymodel
        self.legendposition = self.data._legendposition
        self.backgroundcolor = self.data._backgroundcolor
        self.transparency = self.data._transparency
        self.filter = self.data._filter

    def add_legend(self, num_legends, contour, **kwargs):
        self.Contour_i = contour
        self.root = contour.root
        allowed_keys = {'legendtype', 'nulcols', 'legendmaxthreshold', 'legendminthreshold',
                        'colorrgb', 'noresultcolor', 'numbers', 'showmax', 'showmaxlocal', 'showmin', 'showminlocal',
                        'entitylabel', 'showbymodel', 'legendposition', 'backgroundcolor', 'transparency', 'filter'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

        class LegendAttributes(object):
            Root = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            LegendType = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            NumCols = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            LegendMaxThreshold = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            LegendMinThreshold = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ColorRgb = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            NoResultColor = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Numbers = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ShowMax = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ShowMaxLocal = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ShowMin = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ShowMinLocal = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            EntityLabel = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            ShowByModel = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            LegendPosition = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            BackGroundColor = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Transparency = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Filter = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            
        Legend = [LegendAttributes() for i in range(num_legends)]

        for i in range(num_legends):  # add all pages
            legend_i = str(i)

            type = 'legend'
            name = type + legend_i
            Legend[i].Root = AnyNode(id=name, type=type, parent=self.Contour_i,
                                   level=None, legend_num=legend_i, data=self.legend)
            Legend[i].Root.level = len(self.Contour_i.ancestors)
            Legend[i].Root.N = len(self.root.leaves)

            type = 'legendtype'
            name = type + legend_i
            Legend[i].LegendType = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                        level=None, legend_num=legend_i, N=None, data=self.legendtype)
            Legend[i].LegendType.level = len(Legend[i].Root.ancestors)
            Legend[i].LegendType.N = len(self.root.leaves)

            type = 'numcols'
            name = type + legend_i
            Legend[i].NumCols = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                           level=None, legend_num=legend_i, N=None, data=self.numcols)
            Legend[i].NumCols.level = len(Legend[i].Root.ancestors)
            Legend[i].NumCols.N = len(self.root.leaves)

            type = 'legendmaxthreshold'
            name = type + legend_i
            Legend[i].LegendMaxThreshold = AnyNode(id=name, type=type, oc=1, parent=self.Contour_i,
                                        level=None, legend_num=legend_i, N=None, data=self.legendmaxthreshold)
            Legend[i].LegendMaxThreshold.level = len(self.Contour_i.ancestors)
            Legend[i].LegendMaxThreshold.N = len(self.root.leaves)

            type = 'legendminthreshold'
            name = type + legend_i
            Legend[i].LegendMinThreshold = AnyNode(id=name, type=type, oc=1, parent=self.Contour_i,
                                                   level=None, legend_num=legend_i, N=None,
                                                   data=self.legendminthreshold)
            Legend[i].LegendMinThreshold.level = len(self.Contour_i.ancestors)
            Legend[i].LegendMinThreshold.N = len(self.root.leaves)

            type = 'colorrgb'
            name = type + legend_i
            Legend[i].ColorRgb = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                        level=None, legend_num=legend_i, N=None, data=self.colorrgb)
            Legend[i].ColorRgb.level = len(Legend[i].Root.ancestors)
            Legend[i].ColorRgb.N = len(self.root.leaves)

            type = 'noresultcolor'
            name = type + legend_i
            Legend[i].NoResultColor = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                         level=None, legend_num=legend_i, N=None, data=self.noresultcolor)
            Legend[i].NoResultColor.level = len(Legend[i].Root.ancestors)
            Legend[i].NoResultColor.N = len(self.root.leaves)

            type = 'numbers'
            name = type + legend_i
            Legend[i].Numbers = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                              level=None, legend_num=legend_i, N=None, data=self.numbers)
            Legend[i].Numbers.level = len(Legend[i].Root.ancestors)
            Legend[i].Numbers.N = len(self.root.leaves)

            type = 'showmax'
            name = type + legend_i
            Legend[i].ShowMax = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                        level=None, legend_num=legend_i, N=None, data=self.showmax)
            Legend[i].ShowMax.level = len(Legend[i].Root.ancestors)
            Legend[i].ShowMax.N = len(self.root.leaves)

            type = 'showmaxlocal'
            name = type + legend_i
            Legend[i].ShowMaxLocal = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                        level=None, legend_num=legend_i, N=None, data=self.showmaxlocal)
            Legend[i].ShowMaxLocal.level = len(Legend[i].Root.ancestors)
            Legend[i].ShowMaxLocal.N = len(self.root.leaves)

            type = 'showmin'
            name = type + legend_i
            Legend[i].ShowMin = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                        level=None, legend_num=legend_i, N=None, data=self.showmin)
            Legend[i].ShowMin.level = len(Legend[i].Root.ancestors)
            Legend[i].ShowMin.N = len(self.root.leaves)

            type = 'showminlocal'
            name = type + legend_i
            Legend[i].ShowMinLocal = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                             level=None, legend_num=legend_i, N=None, data=self.showminlocal)
            Legend[i].ShowMinLocal.level = len(Legend[i].Root.ancestors)
            Legend[i].ShowMinLocal.N = len(self.root.leaves)

            type = 'entitylabel'
            name = type + legend_i
            Legend[i].EntityLabel = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                             level=None, legend_num=legend_i, N=None, data=self.entitylabel)
            Legend[i].EntityLabel.level = len(Legend[i].Root.ancestors)
            Legend[i].EntityLabel.N = len(self.root.leaves)

            type = 'showbymodel'
            name = type + legend_i
            Legend[i].ShowByModel = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                            level=None, legend_num=legend_i, N=None, data=self.showbymodel)
            Legend[i].ShowByModel.level = len(Legend[i].Root.ancestors)
            Legend[i].ShowByModel.N = len(self.root.leaves)

            type = 'legendposition'
            name = type + legend_i
            Legend[i].LegendPosition = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                            level=None, legend_num=legend_i, N=None, data=self.legendposition)
            Legend[i].LegendPosition.level = len(Legend[i].Root.ancestors)
            Legend[i].LegendPosition.N = len(self.root.leaves)

            type = 'backgroundcolor'
            name = type + legend_i
            Legend[i].BackGroundColor = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                               level=None, legend_num=legend_i, N=None, data=self.backgroundcolor)
            Legend[i].BackGroundColor.level = len(Legend[i].Root.ancestors)
            Legend[i].BackGroundColor.N = len(self.root.leaves)

            type = 'transparency'
            name = type + legend_i
            Legend[i].Transparency = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                                level=None, legend_num=legend_i, N=None, data=self.transparency)
            Legend[i].Transparency.level = len(Legend[i].Root.ancestors)
            Legend[i].Transparency.N = len(self.root.leaves)

            type = 'filter'
            name = type + legend_i
            Legend[i].Filter = AnyNode(id=name, type=type, oc=1, parent=Legend[i].Root,
                                             level=None, legend_num=legend_i, N=None, data=self.filter)
            Legend[i].Filter.level = len(Legend[i].Root.ancestors)
            Legend[i].Filter.N = len(self.root.leaves)


        return Legend

    def modify_legend(self, legend_mod):
        _global_callback('legend', legend_mod)

    def modify_legendtype(self, legend_mod):
        _global_callback('legendtype', legend_mod)
    
    def modify_numcols(self, legend_mod):
        _global_callback('numcols', legend_mod)
    
    def modify_legendmaxthreshold(self, legend_mod):
        _global_callback('legendmaxthreshold', legend_mod)
    
    def modify_legendminthreshold(self, legend_mod):
        _global_callback('legendminthreshold', legend_mod)
    
    def modify_colorrgb(self, colorrgb_mod):
        _global_callback('colorrgb', colorrgb_mod)
        
    def modify_noresultcolor(self, noresultcolor_mod):
        _global_callback('noresultcolor', noresultcolor_mod)
        
    def modify_numbers(self, numbers_mod):
        _global_callback('numbers', numbers_mod)
    
    def modify_showmax(self, showmax_mod):
        _global_callback('showmax', showmax_mod)
    
    def modify_showmaxlocal(self, showmaxlocal_mod):
        _global_callback('showmaxlocal', showmaxlocal_mod)

    def modify_showmin(self, showmin_mod):
        _global_callback('showmin', showmin_mod)

    def modify_showminlocal(self, showminlocal_mod):
        _global_callback('showminlocal', showminlocal_mod)
    
    def modify_entitylabel(self, entitylabel_mod):
        _global_callback('entitylabel', entitylabel_mod)
    
    def modify_showbymodel(self, showbymodel_mod):
        _global_callback('showbymodel', showbymodel_mod)
    
    def modify_legendposition(self, legendposition_mod):
        _global_callback('legendposition', legendposition_mod)
    
    def modify_backgroundcolor(self, backgroundcolor_mod):
        _global_callback('backgroundcolor', backgroundcolor_mod)
    
    def modify_transparency(self, transparency_mod):
        _global_callback('transparency', transparency_mod)
    
    def modify_filter(self, filter_mod):
        _global_callback('filter', filter_mod)
        

class NoteState(object):

    def __init__(self, **kwargs):
        self._note = '"On", "Model Info"'
        self._transparent = 'On'
        self._autohide = 'Off'
        self._anchortoscreen = 'On'
        self._fillcolor = '31'
        self._textcolor = '1'
        self._attach = 'WINDOW'
        self._position = '0.5, 0.5'
        self._text = '{for (i = 0; i != numpts(window.modeltitlelist); ++i) }\\n{window.modelidlist[i]}: {window.modeltitlelist[i]}\\n{window.loadcaselist[i]} : {window.simulationsteplist[i]} : {window.framelist[i]}\\n{endloop}'
        self._font = '"noto sans", "regular", "regular", 10'
        self._color = '1'
        self._borderwidth = '0'
        self._shape = 'Rectangle'
        self._notealignment = 'Right'
        self._noteanchor = '"Right", "Top"'
        self._titleflag = 'Yes'
        
        self._observers_note = []
        self._observers_transparent = []
        self._observers_autohide = []
        self._observers_anchortoscreen = []
        self._observers_fillcolor = []
        self._observers_textcolor = []
        self._observers_attach = []
        self._observers_position = []
        self._observers_text = []
        self._observers_font = []
        self._observers_color = []
        self._observers_borderwidth = []
        self._observers_shape = []
        self._observers_notealignment = []
        self._observers_noteanchor = []
        self._observers_titleflag = []

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, data):
        self._note = data
        for callback in self._observers_note:
            callback(self._note)

    @property
    def transparent(self):
        return self._transparent

    @transparent.setter
    def transparent(self, data):
        self._transparent = data
        for callback in self._observers_transparent:
            callback(self._transparent)

    @property
    def autohide(self):
        return self._autohide

    @autohide.setter
    def autohide(self, data):
        self._autohide = data
        for callback in self._observers_autohide:
            callback(self._autohide)

    @property
    def anchortoscreen(self):
        return self._anchortoscreen

    @anchortoscreen.setter
    def anchortoscreen(self, data):
        self._anchortoscreen = data
        for callback in self._observers_anchortoscreen:
            callback(self._anchortoscreen)

    @property
    def fillcolor(self):
        return self._fillcolor

    @fillcolor.setter
    def fillcolor(self, data):
        self._fillcolor = data
        for callback in self._observers_fillcolor:
            callback(self._fillcolor)

    @property
    def textcolor(self):
        return self._textcolor

    @textcolor.setter
    def textcolor(self, data):
        self._textcolor = data
        for callback in self._observers_textcolor:
            callback(self._textcolor)

    @property
    def attach(self):
        return self._attach

    @attach.setter
    def attach(self, data):
        self._attach = data
        for callback in self._observers_attach:
            callback(self._attach)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, data):
        self._position = data
        for callback in self._observers_position:
            callback(self._position)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, data):
        self._text = data
        for callback in self._observers_text:
            callback(self._text)

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, data):
        self._font = data
        for callback in self._observers_font:
            callback(self._font)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, data):
        self._color = data
        for callback in self._observers_color:
            callback(self._color)

    @property
    def borderwidth(self):
        return self._borderwidth

    @borderwidth.setter
    def borderwidth(self, data):
        self._borderwidth = data
        for callback in self._observers_borderwidth:
            callback(self._borderwidth)

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, data):
        self._shape = data
        for callback in self._observers_shape:
            callback(self._shape)

    @property
    def notealignment(self):
        return self._notealignment

    @notealignment.setter
    def notealignment(self, data):
        self._notealignment = data
        for callback in self._observers_notealignment:
            callback(self._notealignment)

    @property
    def noteanchor(self):
        return self._noteanchor

    @noteanchor.setter
    def noteanchor(self, data):
        self._noteanchor = data
        for callback in self._observers_noteanchor:
            callback(self._noteanchor)

    @property
    def titleflag(self):
        return self._titleflag

    @titleflag.setter
    def titleflag(self, data):
        self._titleflag = data
        for callback in self._observers_titleflag:
            callback(self._titleflag)

    def bind_to_note(self, callback):
        self._observers_note.append(callback)

    def bind_to_transparent(self, callback):
        self._observers_transparent.append(callback)
    
    def bind_to_autohide(self, callback):
        self._observers_autohide.append(callback)
    
    def bind_to_anchortoscreen(self, callback):
        self._observers_anchortoscreen.append(callback)
    
    def bind_to_fillcolor(self, callback):
        self._observers_fillcolor.append(callback)
    
    def bind_to_textcolor(self, callback):
        self._observers_textcolor.append(callback)
    
    def bind_to_attach(self, callback):
        self._observers_attach.append(callback)
    
    def bind_to_position(self, callback):
        self._observers_position.append(callback)
    
    def bind_to_text(self, callback):
        self._observers_text.append(callback)
    
    def bind_to_font(self, callback):
        self._observers_font.append(callback)
    
    def bind_to_color(self, callback):
        self._observers_color.append(callback)
    
    def bind_to_borderwidth(self, callback):
        self._observers_borderwidth.append(callback)

    def bind_to_shape(self, callback):
        self._observers_shape.append(callback)
    
    def bind_to_notealignment(self, callback):
        self._observers_notealignment.append(callback)
    
    def bind_to_noteanchor(self, callback):
        self._observers_noteanchor.append(callback)
    
    def bind_to_titleflag(self, callback):
        self._observers_titleflag.append(callback)


class Note(object):

    def __init__(self, data, **kwargs):
        self.data = data
        self.data.bind_to_note(self.modify_note)
        self.data.bind_to_transparent(self.modify_transparent)
        self.data.bind_to_autohide(self.modify_autohide)
        self.data.bind_to_anchortoscreen(self.modify_anchortoscreen)
        self.data.bind_to_fillcolor(self.modify_fillcolor)
        self.data.bind_to_textcolor(self.modify_textcolor)
        self.data.bind_to_attach(self.modify_attach)
        self.data.bind_to_position(self.modify_position)
        self.data.bind_to_text(self.modify_text)
        self.data.bind_to_font(self.modify_font)
        self.data.bind_to_color(self.modify_color)
        self.data.bind_to_borderwidth(self.modify_borderwidth)
        self.data.bind_to_shape(self.modify_shape)
        self.data.bind_to_notealignment(self.modify_notealignment)
        self.data.bind_to_noteanchor(self.modify_noteanchor)
        self.data.bind_to_titleflag(self.modify_titleflag)

        self.note = self.data._note
        self.transparent = self.data._transparent
        self.autohide = self.data._autohide
        self.anchortoscreen = self.data._anchortoscreen
        self.fillcolor = self.data._fillcolor
        self.textcolor = self.data._textcolor
        self.attach = self.data._attach
        self.position = self.data._position
        self.text = self.data._text
        self.font = self.data._font
        self.color = self.data._color
        self.borderwidth = self.data._borderwidth
        self.shape = self.data._shape
        self.notealignment = self.data._notealignment
        self.noteanchor = self.data._noteanchor
        self.titleflag = self.data._titleflag

    def add_note(self, num_notes, graphic, **kwargs):
        self.Graphic_i = graphic
        self.root = graphic.root
        allowed_keys = {'transparent', 'note', 'autohide', 'anchortoscreen', 'fillcolor', 'textcolor', 'attach', 
                        'position', 'text', 'font', 'color', 'borderwidth', 'shape', 'notealignment', 'noteanchor',
                        'titleflag'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

        class NoteAttributes(object):
            Root = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Transparent = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            AutoHide = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            AnchorToScreen = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            FillColor = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            TextColor = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Attach = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Position = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Text = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Font = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Color = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            BorderWidth = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            Shape = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            NoteAlignment = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            NoteAnchor = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            TitleFlag = [AnyNode(id=None, N=None, type=None, parent=None, level=None, window_num=None, data=None)]
            
        Note = [NoteAttributes() for i in range(num_notes)]

        for i in range(num_notes):  # add all pages
            note_i = str(i)

            type = 'note'
            name = type + note_i
            Note[i].Root = AnyNode(id=name, type=type, parent=self.Graphic_i,
                                   level=None, note_num=note_i, data=self.note)
            Note[i].Root.level = len(self.Graphic_i.ancestors)
            Note[i].Root.N = len(self.root.leaves)

            type = 'transparent'
            name = type + note_i
            Note[i].Transparent = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                        level=None, note_num=note_i, N=None, data=self.transparent)
            Note[i].Transparent.level = len(Note[i].Root.ancestors)
            Note[i].Transparent.N = len(self.root.leaves)

            type = 'autohide'
            name = type + note_i
            Note[i].AutoHide = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                          level=None, note_num=note_i, N=None, data=self.autohide)
            Note[i].AutoHide.level = len(Note[i].Root.ancestors)
            Note[i].AutoHide.N = len(self.root.leaves)

            type = 'anchortoscreen'
            name = type + note_i
            Note[i].AnchorToScreen = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                       level=None, note_num=note_i, N=None, data=self.anchortoscreen)
            Note[i].AnchorToScreen.level = len(Note[i].Root.ancestors)
            Note[i].AnchorToScreen.N = len(self.root.leaves)

            type = 'fillcolor'
            name = type + note_i
            Note[i].FillColor = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                             level=None, note_num=note_i, N=None, data=self.fillcolor)
            Note[i].FillColor.level = len(Note[i].Root.ancestors)
            Note[i].FillColor.N = len(self.root.leaves)

            type = 'textcolor'
            name = type + note_i
            Note[i].TextColor = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                        level=None, note_num=note_i, N=None, data=self.textcolor)
            Note[i].TextColor.level = len(Note[i].Root.ancestors)
            Note[i].TextColor.N = len(self.root.leaves)

            type = 'attach'
            name = type + note_i
            Note[i].Attach = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                        level=None, note_num=note_i, N=None, data=self.attach)
            Note[i].Attach.level = len(Note[i].Root.ancestors)
            Note[i].Attach.N = len(self.root.leaves)

            type = 'position'
            name = type + note_i
            Note[i].Position = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                     level=None, note_num=note_i, N=None, data=self.position)
            Note[i].Position.level = len(Note[i].Root.ancestors)
            Note[i].Position.N = len(self.root.leaves)

            type = 'text'
            name = type + note_i
            Note[i].Text = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                       level=None, note_num=note_i, N=None, data=self.text)
            Note[i].Text.level = len(Note[i].Root.ancestors)
            Note[i].Text.N = len(self.root.leaves)

            type = 'font'
            name = type + note_i
            Note[i].Font = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                   level=None, note_num=note_i, N=None, data=self.font)
            Note[i].Font.level = len(Note[i].Root.ancestors)
            Note[i].Font.N = len(self.root.leaves)

            type = 'color'
            name = type + note_i
            Note[i].Color = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                   level=None, note_num=note_i, N=None, data=self.color)
            Note[i].Color.level = len(Note[i].Root.ancestors)
            Note[i].Color.N = len(self.root.leaves)

            type = 'borderwidth'
            name = type + note_i
            Note[i].BorderWidth = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                    level=None, note_num=note_i, N=None, data=self.borderwidth)
            Note[i].BorderWidth.level = len(Note[i].Root.ancestors)
            Note[i].BorderWidth.N = len(self.root.leaves)

            type = 'shape'
            name = type + note_i
            Note[i].Shape = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                          level=None, note_num=note_i, N=None, data=self.shape)
            Note[i].Shape.level = len(Note[i].Root.ancestors)
            Note[i].Shape.N = len(self.root.leaves)

            type = 'notealignment'
            name = type + note_i
            Note[i].NoteAlignment = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                    level=None, note_num=note_i, N=None, data=self.notealignment)
            Note[i].NoteAlignment.level = len(Note[i].Root.ancestors)
            Note[i].NoteAlignment.N = len(self.root.leaves)

            type = 'noteanchor'
            name = type + note_i
            Note[i].NoteAnchor = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                            level=None, note_num=note_i, N=None, data=self.noteanchor)
            Note[i].NoteAnchor.level = len(Note[i].Root.ancestors)
            Note[i].NoteAnchor.N = len(self.root.leaves)

            type = 'titleflag'
            name = type + note_i
            Note[i].TitleFlag = AnyNode(id=name, type=type, oc=1, parent=Note[i].Root,
                                         level=None, note_num=note_i, N=None, data=self.titleflag)
            Note[i].TitleFlag.level = len(Note[i].Root.ancestors)
            Note[i].TitleFlag.N = len(self.root.leaves)

        return Note

    def modify_note(self, note_mod):
        _global_callback('note', note_mod)
        
    def modify_transparent(self, note_mod):
        _global_callback('transparent', note_mod)
    
    def modify_autohide(self, note_mod):
        _global_callback('autohide', note_mod)
    
    def modify_anchortoscreen(self, note_mod):
        _global_callback('anchortoscreen', note_mod)
    
    def modify_fillcolor(self, note_mod):
        _global_callback('fillcolor', note_mod)
    
    def modify_textcolor(self, note_mod):
        _global_callback('textcolor', note_mod)
    
    def modify_attach(self, note_mod):
        _global_callback('attach', note_mod)
    
    def modify_position(self, note_mod):
        _global_callback('position', note_mod)
    
    def modify_text(self, note_mod):
        _global_callback('text', note_mod)
    
    def modify_font(self, note_mod):
        _global_callback('font', note_mod)
    
    def modify_color(self, note_mod):
        _global_callback('color', note_mod)
    
    def modify_borderwidth(self, note_mod):
        _global_callback('borderwidth', note_mod)
    
    def modify_shape(self, note_mod):
        _global_callback('shape', note_mod)
    
    def modify_notealignment(self, note_mod):
        _global_callback('notealignment', note_mod)
    
    def modify_noteanchor(self, note_mod):
        _global_callback('noteanchor', note_mod)
    
    def modify_titleflag(self, note_mod):
        _global_callback('titleflag', note_mod)


class Write(object):

    def __init__(self, hvsession):
        self.writeroot = hvsession.root
        # print(RenderTree(self.writeroot))

    def mvw(self, name, writedir, **kwargs):
        session_list = []
        mysession = open(writedir+'/'+name, 'w')
        line_no = 0
        for node in PreOrderIter(self.writeroot):
            if not _is_rightest_child(node) and not _has_children(node):
                for line in _get_block(node):
                    print(line)
                    mysession.write('\n'+line)
            elif not _is_rightest_child(node) and _has_children(node):
                print(_get_block(node)[0])
                if line_no == 0:
                    mysession.write(_get_block(node)[0])
                else:
                    mysession.write('\n'+_get_block(node)[0])
            elif _is_rightest_child(node) and not _has_children(node):  # extend this block to close all ancestors too
                for line in _get_block(node):
                    print(line)
                    mysession.write('\n'+line)
                print(_get_block(node.parent)[1])
                mysession.write('\n'+_get_block(node.parent)[1])
                ancestors = list(node.ancestors)
                ancestors.reverse()
                for i in range(len(ancestors)):
                    if _is_rightest_child(ancestors[i]) and ancestors[i].id != 'root':
                        print(_get_block(ancestors[i].parent)[1])
                        mysession.write('\n'+_get_block(ancestors[i].parent)[1])
                    else:
                        break
            elif _is_rightest_child(node) and _has_children(node):
                print(_get_block(node)[0])
                if line_no == 0:
                    mysession.write(_get_block(node)[0])
                else:
                    mysession.write('\n'+_get_block(node)[0])

            line_no = line_no + 1
        # file = open(writedir+'/'+name,'w')
        # print(RenderTree(self.writeroot))

        mysession.close()
        print('Session successfully written to '+writedir+name+'.\n')
        return


if __name__ == '__main__':


    # ------------------------------------------------------------------------------------------------------------------
    # EXAMPLE
    # ------------------------------------------------------------------------------------------------------------------

    a = time.time()

    # ------------------------------------------------------------------------------------------------------------------
    # Add and modify pages to session
    # ------------------------------------------------------------------------------------------------------------------


    gui1 = 'HyperWorks'
    version1 = '19'
    graphics1 = ['C:/Users/Yumitomo/Projects/HyperWorks/mv_hv_hg/mv_hv_hg/animation/bezel_iter2.h3d']
    results1 = ['C:/Users/Yumitomo/Projects/HyperWorks/mv_hv_hg/mv_hv_hg/animation/bezel_iter2.h3d']

    pages_state = PageState(gui1, version1, graphics1, results1)
    pages_root = Page(pages_state)

    pages = pages_root.add_pages(1)  # add pages to session root

    pages_state.title = (pages[0].Title, 'Renamed to THIS!')  # change title of specified page
    pages_state.animator = (pages[0].Animator, 'Static')  # Change animation type of specified page
    pages_state.titlefont = (pages[0].TitleFont, ('Noto Sans', 1, 0, 12))  # change font of title of specified page

    # ------------------------------------------------------------------------------------------------------------------
    # Add and modify windows to pages
    # ------------------------------------------------------------------------------------------------------------------

    windows_state = WindowState()  # initialize a state object for all windows of all pages
    windows_root = Window(windows_state)  # initialize a root object for all windows of all pages

    page0_root = pages[0].Root
    windows = windows_root.add_windows(1, page0_root, 1)

    # ------------------------------------------------------------------------------------------------------------------
    # Add and modify graphics to windows
    # ------------------------------------------------------------------------------------------------------------------

    graphics_state = GraphicState()  # initialize a graphics state object for all graphics on all windows and pages
    graphics_root = Graphic(graphics_state)  # initialize graphics root object for all graphics on all windows and pages

    window0_root = windows[0].Root  # get window 0 root node
    window0_graphics = graphics_root.add_graphics(1, window0_root)  # add 1 graphic to window 0 root node

    # ------------------------------------------------------------------------------------------------------------------
    # Add and modify models to graphics
    # ------------------------------------------------------------------------------------------------------------------

    models_state = ModelState()
    models_root = Model(models_state)

    window0_graphic0_root = window0_graphics[0].Root  # get graphic 0 root node
    window0_graphic0_models = models_root.add_model(1, window0_graphic0_root)  # add 1 model to graphic 0 root node

    models_state.scale = (window0_graphic0_models[0].Scale, '1000, 1000, 1000')
    # ------------------------------------------------------------------------------------------------------------------
    # Add and modify results to models
    # ------------------------------------------------------------------------------------------------------------------

    results_state = ResultState()
    results_root = Result(results_state)

    model0_root = window0_graphic0_models[0].Root  # get model 0 root
    model0_results = results_root.add_result(1, model0_root)  # add 1 result to model 0 root

    results_state.currentsubcase = (model0_results[0].CurrentSubcase, '1, 0')  # change subcase to step 1, increment 0

    # ------------------------------------------------------------------------------------------------------------------
    # Add and modify parts to models
    # ------------------------------------------------------------------------------------------------------------------

    parts_state = PartState()
    parts_root = Part(parts_state)

    model0_root = window0_graphic0_models[0].Root
    model0_parts = parts_root.add_part(2, model0_root)

    # ------------------------------------------------------------------------------------------------------------------
    # Add and modify groups to models
    # ------------------------------------------------------------------------------------------------------------------

    groups_state = GroupState()  # initialize a groups state object for all groups on all graphics, windows, and pages
    groups_root = Group(groups_state)  # initialize groups root object for all groups on all graphics, windows, and pages

    model0_root = window0_graphic0_models[0].Root  # get model 0 root
    model0_groups_1d = groups_root.add_group(1, 1, model0_root)  # add 1 1d group to model 0
    model0_groups_2d = groups_root.add_group(1, 2, model0_root)  # add 1 2d group to model 0

    # ------------------------------------------------------------------------------------------------------------------
    # Add and modify contours to models
    # ------------------------------------------------------------------------------------------------------------------

    contours_state = ContourState()  # initialize a contours state object for all contours on all graphics, windows, and pages
    contours_root = Contour(contours_state)  # initialize contours root object for all contours on all graphics, windows, and pages

    model0_root = window0_graphic0_models[0].Root  # get model 0 root

    model0_contours = contours_root.add_contour(1, model0_root) #default result type is displacement
    contours_state.datacomponent = (model0_contours[0].DataComponent, 'Y')
    contours_state.multiplelayers = (model0_contours[0].MultipleLayers, 'true')
    contours_state.averageacrossparts = (model0_contours[0].AverageAcrossParts, 'On')
    # model0_contours = contours_root.add_contour(1, model0_root, resulttype='Element Stresses (2D & 3D)', datacomponent='vonMises')

    # ------------------------------------------------------------------------------------------------------------------
    # Add and modify legends to contours
    # ------------------------------------------------------------------------------------------------------------------

    legends_state = LegendState()  # initialize a legends state object for all legends on all graphics, windows, and pages
    legends_root = Legend(legends_state)  # initialize legends root object for all legends on all graphics, windows, and pages

    contour0_root = model0_contours[0].Root
    contour0_legends = legends_root.add_legend(1, contour0_root)  # default result type is displacement

    legends_state.numcols = (contour0_legends[0].NumCols, '9')
    legends_state.noresultcolor = (contour0_legends[0].NoResultColor, '0, 0, 0')
    legends_state.legendminthreshold = (contour0_legends[0].LegendMinThreshold, ('On, 0'))
    legends_state.legendmaxthreshold = (contour0_legends[0].LegendMaxThreshold, ('"On", 3.8E-4'))

    # ------------------------------------------------------------------------------------------------------------------
    # Add and modify notes to graphics
    # ------------------------------------------------------------------------------------------------------------------

    notes_state = NoteState()  # initialize a notes state object for all notes on all graphics, windows, and pages
    notes_root = Note(notes_state)  # initialize notes root object for all notes on all graphics, windows, and pages

    graphic0_notes = notes_root.add_note(1, window0_graphic0_root)  # default result type is displacement

    notes_state.note = (graphic0_notes[0].Root, '"On", "Model Info"')
    
    # ------------------------------------------------------------------------------------------------------------------
    # Write session to file
    # ------------------------------------------------------------------------------------------------------------------

    location1 = 'C:/Users/Yumitomo/Projects/hyperpy/'
    name1 = 'test.mvw'
    Write(pages_root).mvw(name1, location1)

    b = time.time()
    print(b - a)
