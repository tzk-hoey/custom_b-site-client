import VideoCardLayout from './VideoCardLayout/index.vue'
import MoreLoader from './MoreLoader/index.vue'
import VideoCard from './VideoCard/index.vue'
import PictureGroup from './PictureGroup/index.vue'


const components = [
    VideoCardLayout,
    MoreLoader,
    VideoCard,
    PictureGroup
]

export const customComponents = {
    install: (app) => {
        for (const component of components) {
            const name = component.__file.split('/').reverse()[1]
            app.component(name, component)
        }
    }
}