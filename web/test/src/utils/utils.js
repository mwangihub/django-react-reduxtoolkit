/**
 * @mwangihub
 * @summary utils module have methods that provide shortcuts
 */

const objectUpdate = (currentObject, updatedObject) => {
    return {
        ...currentObject, ...updatedObject
    }
}
const setItemLocalStorage = (items = []) => {
    let obj = Object.fromEntries(items)
    for (const key in obj) {
        if (obj.hasOwnProperty(key)) {
            localStorage.setItem(key, obj[key]);
        }
    }
}
const getItemLocalStorage = (items = []) => {
    const obj = {}
    if (items.length) {
        items.forEach(item => {
            obj[item] = localStorage.getItem(item)
        });
    }
    return obj
}
const removeItemLocalStorage = (items = []) => {
    if (items.length) {
        items.forEach(item => {
            localStorage.removeItem(item)
        });
    }
}


const Utils = {
    objectUpdate,
    removeItemLocalStorage,
    getItemLocalStorage,
    setItemLocalStorage,
}
export default Utils;