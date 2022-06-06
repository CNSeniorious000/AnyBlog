const do_nothing = () => false

function disable(element) {
    element.oncontextmenu = do_nothing
    element.onbeforecopy = do_nothing
    element.ondragstart = do_nothing
    element.ondragend = do_nothing
    element.onselect = do_nothing
    element.onclick = do_nothing
    element.oncopy = do_nothing
}
