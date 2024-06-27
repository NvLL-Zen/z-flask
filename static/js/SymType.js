const sleep = ms => new Promise(r => setTimeout(r, ms));

const xRevType = async (element, symbol) => {
    let iteration = element.textContent.length
    let oldstr = element.textContent.split('')
    for(let i = 0; i < iteration; i++){
        oldstr[i] = symbol
        element.innerHTML = oldstr.join('')
        await sleep(50)
    }
}

const xType = async (element, text, symbol) => {
    if(text.length > element.textContent.length){
        let iter = text.length - element.textContent.length
        let replaceString = element.textContent.split('')
        for(let i =0; i < iter; i++){
            replaceString.push(symbol)
            element.innerHTML = replaceString.join('')
            await sleep(50)
        }
        await sleep(iter*50)
    } else if (text.length < element.textContent.length){
        let iter = element.textContent.length - text.length 
        let replaceString = element.textContent.split('')
        for(let i =0; i < iter; i++){
            replaceString.pop()
            element.innerHTML = replaceString.join('')
            await sleep(50)
        }
        await sleep(iter*50)
    }
    let iteration = element.textContent.length
    let elementString = element.textContent.split('')
    let newString = text.split('')
    for(let i = 0; i < iteration; i++){
        elementString[i] = newString[i]
        element.innerHTML = elementString.join('')
        await sleep(50)
    }
}

export {sleep, xType, xRevType}