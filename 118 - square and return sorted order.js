function squareAndSort(arr) {
    const answer = arr.map((num) => {
        return num * num
    })
    answer.sort((a, b) => {
        return a - b
    })
    return answer
}

console.log(squareAndSort([-9, -2, 0, 2, 3]))
