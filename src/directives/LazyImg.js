import { useIntersectionObserver } from '@vueuse/core'

export const LazyImg = {
    name: 'lazy-img',
    mounted: (el, binding) => {
        const {stop} = useIntersectionObserver(
            el,
            ([{ isIntersecting }]) =>  {
                if (isIntersecting) {
                    el.src = binding.value
                    stop()
                }
            }
        )
    }
}