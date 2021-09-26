export const actions = {
    nuxtServerInit({ commit }, { app }) {
        const token = app.$cookies.get('token')
        commit('users/LOGIN', token)
    },
}