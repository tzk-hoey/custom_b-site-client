import { createRouter, createWebHistory } from 'vue-router'
import Layout from '@/views/Layout/index.vue'
import Hot from '@/views/Hot/index.vue'
import Config from '@/views/Config/index.vue'
import Reply from '@/views/Message/Reply/index.vue'
import Approval from '@/views/Message/Approval/index.vue'
import Dynamic from '@/views/Dynamic/index.vue'
import Follow from '@/views/Follow/index.vue'
import Test from '@/views/Test.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/123',
      component: Test
    },
    {
      path: '/',
      component: Layout,
      redirect: '/config',
      children: [
        {
          path: 'hot',
          component: Hot,
          meta: {title: '热门'}
        },
        {
          path: 'config',
          component: Config,
          meta: {title: '设置'}
        },
        {
          path: 'reply',
          component: Reply,
          meta: {title: '回复'}
        },
        {
          path: 'approval',
          component: Approval,
          meta: {title: '点赞'}
        },
        {
          path: 'dynamic/:type/:mid?',
          component: Dynamic,
          meta: {title: '动态'}
        },
        {
          path: 'follow',
          component: Follow,
          meta: {title: '关注'}
        }
      ]
    }
  ]
})

export default router
