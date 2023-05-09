# Market Research Prototype

The Market Research Prototype is a prototype application designed for two statigic objectives.

- Functional

    To provide the marketing department more independence and flexibility in gathering and modelling research data.

- Technical

    To demonsrate the potential effectiveness and efficiency of using Python for Big Data reporting projects.

This app loads data from csv files already downloaded and customised from the origin on the World Bank website. As on the website each file contains a different demographic for all countries across the globe.  In addition, it contains groupings of 
countries into regions.  The countries and regions are identical across all demographic files. For this prototype, the regions have been appended to each country record to simplify the loading and reporting process.

The prototype contains only 3 demographic files to demonstrate the ability to report
on large sets of public data summed by region and demographic. Currently, the app
summarises the demographic values by region and for a range of years downloaded.

For the production version, as envisioned, the user will select and download the
demographic statistic files which will then be directly loaded into the app without the need for further file manipulation by IT in order for the user to report on. In addition to being able to include more demographics, the user will be able to:
- Rank the impact of each demographic in the summary
- Rank countries according to their demographics


#Table of Contents

1. [UX](#ux-planes)
    - [Background Story](background-story)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
2. [Features](#features)
3. [Testing](#testing)
4. [Deployment](#deployment)
5. [Credit and Contact](#credit-and-contact)

# UX Planes
# Background Story

The marketing department of a company requested a tool to consolidate large sets of data into meaningful categories of information. They routinely use research data from the World Bank's World Development Indicators which is available to download as a CSV but too large for them to use for spreadsheet modelling. The functional goal is to provide the user more independence and flexibility in gathering and modelling research data.

The company has decided to use this project to also test the use of Python as a potential new tool for future big data/report generation projects. Thus this project has a secondary goal of demonstrating the effectiveness and efficiency of the Python language.
## Strategy

The following is a wish list of application features and functions drawn from user interviews:

1. Download and import demographic data files (files all contain country and regional statistics).
2. Model the data to select the best countries for their marketing plan.
3. Summarise the large data into analytical groups of information.
4. View the results of the summarisation.
5. Import analytical information to spreadsheet for additional modelling.

## Scope

Upon further consultation with the user community and key stakeholders, it was agreed to go forward with a pilot project of the following scope:

1. Three demographics:
  1. Population
  2. Urbanisation
  3. Disposable Income
2. The modelling would allow them to query the top 5 countries for each demographic and for year-on-year change combined for all countries and varying by:
  1. the weight of each demographic (out of 100%)
  2. range of years
  3. countries

### Feasibility

Based on the timeline, budget, and resources the scope was further refined to:

- Regional, not country, summarisation
- 100% of each demographic (no weighting)

## Structure

[Data Structures](https://drive.google.com/file/d/1bmDEPD3KhVa_wrLIyS6WBPk9UtRFXFSf/view?usp=sharing)

[Process Design](https://drive.google.com/file/d/1aRZ9r7KIuD9CYvLSRKJ-CEYSc5KUKemT/view?usp=share_link)

# Features
## App introduction
![Introduction Screen](/assets/docs/Start_Screen.png)


## User name capture (and validation) for:
    - log entry recording
    - output file naming
    - app personalisation
![Name Validation Screen](/assets/docs/Name_Validation.png)


## Report Configuration (and validation)
### Range of years
![Range of Years - validation 1](/assets/docs/Year_Validation1.png)
![Range of Years - validation 2](/assets/docs/Year_Validation2.png)

### Regions
![Region selection - validation 1](/assets/docs/Region_Validation1.png)
![Region selection - validation 2](/assets/docs/Region_Validation2.png)


## Summary report output
### display
![Report output screen](/assets/docs/Rpt_Output.png)
### csv file
![Report output CSV file](/assets/docs/Rpt_CSV.png)

#Testing
Unit testing was done at the completion of each function and a full app set of 
tests was completed before deployment.
Although, mainly due to issues (loss of records and time) with CodeAnywhere, below is a link to one of my testing logs with examples of the tests I ran
and the recent results.

[Test Logs](https://docs.google.com/spreadsheets/d/12p2A_JUdu9wUnjL-U9RsZCn-rrAWA0j2OMrFc7A6VPs/edit?usp=share_link)

Name Validation Example
![Name error example](/assets/docs/Name%20Errors.png)

#Deployment
### Github 
**Requirements:**
- A free GitHub account.

### Github Instructions
1. Log in to your GitHub account.
2. navigate to [https://github.com/Richard5P/market_research](https://github.com/Richard5P/market_research).
3. You can set up your own repository and copy or clone it, or you fork the repository.
4. `git add`, `git commit` and `git push` to a GitHub repository, if necessary.
5. GitHub pages will update from the master branch by default.
6. Go to the **Settings** page of the repository.
7. Scroll down to the **Github Pages** section.
8. Select the Master Branch as the source and **Confirm** the selection.

### Heroku
No account needed to run.
To run go to [https://market-research.herokuapp.com/](https://market-research.herokuapp.com/)