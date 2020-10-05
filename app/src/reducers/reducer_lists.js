import { FETCH_LIBRARY } from '../actions/index'

const initialState = {
    libraryList: [],
};

export default function (state = initialState, action) {
    switch(action.type) {
        case FETCH_LIBRARY:
            return { ...state, libraryList: action.payload.data };
        default:
            return state;
    }
}