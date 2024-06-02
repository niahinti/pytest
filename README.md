Hello World, this is a demo Test Automation project using Python, Pytest and Selenium.

It includes a Web UI and an API Feature with Scenarios written in Cucumber.

The web UI test opens a Chrome WebDriver, goes to a SoftServe URL, searches for a term, opens a search result from a list, switches to the new tab and validates a text.

The API feature sends a GET request to a URL and receives the names of the astronauts currently orbiting on the International Space Station. How cool is that?


We can validate the status code and content in a separate validations class and do some assertions with test data from the Scenario outline examples.

I used Page Object Model to define the page classes with inheritance, with Layout as the base parent class because it can be found through all other pages.

I also used a conftest.py file to define the fixtures, to initialize the browser or store information as scenario context.

Here's a preview of the test execution:
![Test Execution](https://github.com/niahinti/pytest/assets/79381055/0356579d-3ab1-49f7-9e28-752f489a229e)

Thanks for taking the time to read this.

Hope you have a nice day and happy coding!!
