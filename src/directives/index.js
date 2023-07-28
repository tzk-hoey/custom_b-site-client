import { LazyImg } from "./LazyImg"

const directives = [
    LazyImg
]

export const customDirectives = {
    install: (app) =>{
        for (const directive of directives){
            app.directive(directive.name, directive)
        }
    }
}