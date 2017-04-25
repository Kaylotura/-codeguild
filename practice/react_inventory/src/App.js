import React, { Component, PropTypes } from 'react';
import SearchBar from './SearchBar'
import StockTable from './StockTable'
import JSONInventory from './JSONInventory'


class App extends Component {
    constructor() {
        super();
        this.state = {
            filterStocked: false,
            searchString: '',
            inCart: [],
            priceTotal: 0,
        };
        this.toggleFilterStocked = this.toggleFilterStocked.bind(this);
        this.updateSearchString = this.updateSearchString.bind(this);
        this.updateInCart = this.updateInCart.bind(this);
  }
  toggleFilterStocked() {
        this.setState({filterStocked: !this.state.filterStocked})
  }
  updateSearchString(value) {
        this.setState({searchString: value})
  }

  updateInCart(ItemName, ItemPrice) {
        let workingCart = this.state.inCart;
        if (workingCart.indexOf(ItemName) === -1) {
            workingCart.push(ItemName);
            this.setState({priceTotal: this.state.priceTotal + ItemPrice})
        } else {
            let itemNameIndex = workingCart.indexOf(ItemName);
            workingCart.splice(itemNameIndex, 1);
            this.setState({priceTotal: this.state.priceTotal - ItemPrice})
        }
        this.setState({workingCart})
  }

  render() {
    return (
        <div>
            <SearchBar
                filterStocked={this.state.filterStocked}
                handleFilterStockedToggle={this.toggleFilterStocked}
                searchString={this.state.searchString}
                handleSearchString={this.updateSearchString}
            />
            <StockTable
                inventory={JSONInventory}
                filterStocked={this.state.filterStocked}
                searchString={this.state.searchString}
                priceTotal={this.state.priceTotal}
                updateInCart={this.updateInCart}
            />
        </div>
    );
  }
}

export default App;