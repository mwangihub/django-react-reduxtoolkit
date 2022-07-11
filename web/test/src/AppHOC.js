import React from 'react'

const AppHOC = (AppComponent, props) => {
    return class extends React.Component {
        render() {
            return <AppComponent {...this.props} {...props} />
        }
    }
}
export default AppHOC;