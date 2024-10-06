# Amortization-calculator
Analyze loan repayment schedules, Calculates fixed monthly payments, principal pay-downs, and interest rates
<!-- Improved compatibility of back to top link: See: https://github.com/ClassicCollins/emzycash/back2top -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out diabetes-prediction-app project. 
*** Thanks for checking out my project!
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for stars-url, forks-url, etc.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links 
-->
[![Forks][forks-shield]][forks-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][twitter-shield]][twitter-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  
  </a>

<h3 align="center">Amortization Calculator Web App</h3>

  <p align="center">
    A Platform for Quantitative Analyses of Financial Instruments!
    <br />
    <a href="https://github.com/ClassicCollins/amortization-calculator"><strong>Explore the Docs »</strong></a>
    <br />
    <br />
    <a href="https://emzycash.streamlitapp.com">Use The App</a>
    ·
    <a href="https://github.com/ClassicCollins/structural-vs-predictive-models/blob/classic/.github/ISSUE_TEMPLATE/bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/ClassicCollins/structural-vs-predictive-models/blob/classic/.github/ISSUE_TEMPLATE/feature-request-form---.md">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Click to View Table of Contents</summary>
  <ol>
    <li>
      <a href="#overview">Overview</a>
      <ul>
        <li><a href="#project-Goal">Project Goal</a></li>
        <li><a href="#technology-stack">Technology Stack</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#how-to-use-the-app">How to Use the App</a></li>
        <li><a href="#outcome">Outcome</a></li>
      </ul>
    </li>
    <li>
      <ul>
        <li><a href="#installation-steps">Installation Steps</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Overview

[![Product Name Screen Shot][product-screenshot]](https://emzycash.streamlitapp.com)

This is a simple Amortization Calculator built using Streamlit. The calculator computes the fixed monthly payment and generates an amortization schedule for a given loan amount, interest rate, and loan term. The amortization schedule breaks down each payment into the principal and interest components, showing how the loan balance is paid down over time.
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Project Goal
`The goal` is to ignite investors' passion for financial assets and take them through the rigorous road of investment
in order to make profitable returns at minimal risk.

### Technology Stack
* `Frontend:` Streamlit
* `Backend:` Python (Pandas, NumPy, numpy_financial)
* `Visualization:` Pandas

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FEATURES -->
### Features
* Input loan parameters: Principal, Annual Interest Rate, and Loan Term.
* Computes the fixed monthly payment.
* Generates an amortization schedule, showing:
  - Month number
  - New principal
  - Interest applied
  - Principal paydown
  - Unpaid principal balance
* Display of the full amortization schedule as a table.
* `Download` option to export the amortization schedule as a CSV file.
<!-- HOW TO USE THE APP -->
## How to Use the App
1. Enter the **loan principal amount** (e.g., $100,000).
2. Provide the **annual interest rate** (e.g., 4% as `0.04`).
3. Set the **loan term** in years (e.g., 30 years).
4. The app will compute and display:
   - The **fixed monthly payment**.
   - The **amortization schedule** (showing month-by-month payments, interest, principal paydown, and remaining balance).
5. Download the **amortization schedule** as a CSV file for further analysis.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- OUTCOME -->
## Outcome
Here’s an example of the output schedule:

| Month | New Principal | Interest Applied | Principal Paydown | Fixed Payment | Unpaid Principal Balance |
|-------|---------------|------------------|-------------------|---------------|-------------------------|
| 1     | $100,000.00    | $333.33          | $1,000.00         | $1,333.33     | $99,000.00              |
| 2     | $99,000.00     | $330.00          | $1,003.33         | $1,333.33     | $97,996.67              |
| ...   | ...            | ...              | ...               | ...           | ...                     |


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- INSTALLATION -->

### Installation Steps

1. Clone the repo:
   ```sh
   git clone https://github.com/ClassicCollins/amortization-calculator.git
   ```
   ```sh
   cd amortization-calculator.git.git
   ```
2. Install required packages:
   ```sh
   pip install -r requirements.txt
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENCE -->
## License
* This project is licensed under the MIT License. See the [LICENSE](https://github.com/ClassicCollins/amortization-calculator/blob/master/LICENSE) file for details
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Collins Emezie Ugwuozor - [@twitter_handle](https://x.com/ClassicCollins2) - ugwuozorcollinsemezie@gmail.com

Project Link: [Amortization calculator](https://www.datascienceportfol.io/collinsugwuozor/projects/1)

Don't forget to give the project a star! Thanks again!

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Python](https://www.python.org)
* [MIT License](https://opensource.org/license/mit)
* [Streamlit](https://share.streamlit.io)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


[issues-shield]: https://img.shields.io/github/issues/ClassicCollins/structural-vs-predictive-models.svg?style=for-the-badge
[issues-url]: https://github.com/ClassicCollins/structural-vs-predictive-models/issues
[forks-shield]: https://img.shields.io/github/forks/ClassicCollins/amortization-calculator.svg?style=for-the-badge
[forks-url]: https://github.com/ClassicCollins/amortization-calculator/forks
[license-shield]: https://img.shields.io/github/license/ClassicCollins/amortization-calculator.svg?style=for-the-badge
[license-url]: https://github.com/ClassicCollins/amortization-calculator/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-white.svg?style=for-the-badge&logo=linkedin&colorB=blue
[linkedin-url]: https://linkedin.com/in/collins-ugwuozor
[twitter-shield]: https://img.shields.io/badge/-Twitter-black.svg?style=for-the-badge&logo=x&colorB=555
[twitter-url]: https://x.com/ClassicCollins2
[product-screenshot]: image/screenshot.png
