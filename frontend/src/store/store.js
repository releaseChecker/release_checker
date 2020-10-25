import { createStore } from 'redux'

export default createStore((state, action) => {
    if (state === undefined) {
        return { author: "ethan.yoo" }
    }
    if (action.type === "TEST") {
        return { ...state, payload: state.author }
    }
    return state
})