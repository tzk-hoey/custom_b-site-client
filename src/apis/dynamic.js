import { request } from '@/utils/request'

export function useDynamicAPI(baseURL){

    const axiosFactory = request(baseURL)

    function getDynamicAPI(page=undefined, offset=undefined, type='all', host_mid=undefined){
        const config = {
            url: '/dynamic',
            method: 'GET',
        }
        config.params = {
            page,
            offset,
            type,
            host_mid
        }
        return axiosFactory(config)
    }

    function getPortalAPI(){
        const config = {
            url: '/portal',
            methdo: 'GET'
        }
        return axiosFactory(config)
    }

    return {
        getDynamicAPI,
        getPortalAPI
    }
}