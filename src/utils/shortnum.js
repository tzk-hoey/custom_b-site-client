export function shortnum(num){
    if (num < 100){
        return num.toString()
    }
    if (num < 100000){
        num = num / 1000
        return num.toFixed(1) + 'K'
    }
    num = num / 1000000
    return num.toFixed(1) + 'M'
}