import 'dragula/dist/dragula.css'
import dragula from 'dragula'

export default ({ app }, inject) => {
  inject('dragula', (arr, obj) => dragula(arr, obj))
}
