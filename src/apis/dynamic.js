import { request } from '@/utils/request'

export function useDynamicAPI(baseURL){

    const axiosFactory = request(baseURL)

    function getDynamicAPI(page=undefined, offset=undefined, type='all'){
        const config = {
            url: '/dynamic',
            method: 'GET',
        }
        config.params = {
            page,
            offset,
            type
        }
        return axiosFactory(config)
    }

    return {
        getDynamicAPI
    }
}