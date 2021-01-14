*** Settings ***

Resource  ../Resources/Amazon.robot
Resource  ../Resources/Common.robot
Suite Setup  Insert Testing Data
Suite Teardown  Cleaning up Data

Test Setup  Begin Web Test
Test Teardown  End Web Test
*** Variables ***
${BROWSER} =  ie
${START_URL} =  http://www.amazon.com
${SEARCH_TERM} =    ferrari 458
${LOGIN_EMAIL} =    Myemail@yahoo.com
${LOGIN_PASSWORD} =    Mypsd1234
*** Test Cases ***
Should be able to login
    Amazon.Login  ${LOGIN_EMAIL}  ${LOGIN_PASSWORD}
    [Tags]  current


User can search a product
    [Documentation]  This is basic info about test
    [Tags]  Somke

    Amazon.Search Products
Logged out user can view a product
    [Tags]
    Amazon.Search Products
    Amazon.Select Product from Search Results

Logged out user can add product to cart
    Amazon.Search Products
    Amazon.Select Product from Search Results
    Amazon.Add Product to Cart

User must sign in to check out
    [Documentation]  This is basic info about test
    [Tags]  current

    Amazon.Search Products
    Amazon.Select Product from Search Results
    Amazon.Add Product to Cart
    Amazon.Begin Checkout


*** Keywords ***
