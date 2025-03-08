Feature: I want to apply for a Software Developer position at Senacor Technologies AG

    Scenario: Navigate to Senacor's website and apply for a Software Developer position
        Given I navigate to "https://www.senacor.com"
        And I accept any of the website's privacy-related controls (even re-appearing ones)
        And I look for a page with job positions
        And I scroll through the page with job positions until the end
        When I find a position as a Software Developer of any seniority level on this jobs page
        Then I should look up details regarding this job position
        And I summarize a short application letter based on the details, but do not intent to submit
