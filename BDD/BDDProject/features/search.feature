Feature: Search
  Scenario: Search for product
    Given buyer is on the OLX homepage
    When  buyer types product in search_input
    Then  search results should be displayed

#Scenario: Search for a product with no results
#  Given buyer is on the OLX homepage
#  When  buyer types product on searchbar
#  Then Error message should be displayed