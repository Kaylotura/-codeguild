/**
 * Created by kaylo on 4/19/2017.
 */
import React, { Component, PropTypes } from 'react';


export default class SearchBar extends Component {
    render() {
        return (
        <form>
            <div>
                <input
                    id="searchStringBox"
                    type="text"
                    placeholder="Search..."
                    onChange={ (event) => this.props.handleSearchString(event.target.value)}
                />
            </div>
            <div>
                <input
                    id="filterStockedCheckBox"
                    type="checkbox"
                    onClick={this.props.handleFilterStockedToggle}
                />
                "Only show products in stock"
            </div>
        </form>
        )
    }
}