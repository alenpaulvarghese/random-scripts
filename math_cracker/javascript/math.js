// CONFIGS

level = 10 // levels that you need to reach

// click start button
document.getElementsByClassName('icon_play')[0].click()

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

for (i = 1; i <= level; ++i) {
    let x = parseInt(document.getElementById('task_x').innerText),
        op = document.getElementById('task_op').innerText,
        y = parseInt(document.getElementById('task_y').innerText)
    guess = document.getElementById('task_res').innerText
    switch (op) {
        case '+':
            answer = x + y
            break
        case '–':
            answer = x - y
            break
        case '/':
            answer = x / y
            break
        case '×':
            answer = x * y
            break
    }
    document
        .getElementsByClassName(
            guess == answer
                ? 'button_correct'
                : 'button_wrong'
        )[0]
        .firstElementChild.click()
    console.log([x, op, y, guess, answer, guess == answer])
    await sleep(100)
}
