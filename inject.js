function getClassMembers(className) {
    let HtmlArray = document.getElementsByClassName(className)
    let ObjectsArray = []
    for (let item of HtmlArray) {
        ObjectsArray.push(item)
    }
    let ItemsArray = ObjectsArray.map(item => item.innerHTML)
    return ItemsArray
}



scripts = {
            getClassMembers : 'asdf',
            findElementPositions : '',
          }