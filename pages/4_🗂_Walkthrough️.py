import streamlit as st
from PIL import Image

st.title("Walkthrough and Logic of Ereditá")
st.divider()
st.markdown("""
All assets can exist under the creation of one single smart contract. However, it's essential to consider the complexity 
and scalability of the system given the variety of assets that may be transferred. As the number of assets and users increases, 
the smart contract's code and requirements may become impractical to maintain or inefficient. It would also make it very unorganized 
and horrible to work with in future scenarios. 

In a complex system such like the one we are proposing, it is better to 
modularize the functionality into multiple smart contracts. Each type of asset or specific functionality 
(such as managing different types of assets or executing transfers) could have its own smart contract. 
This approach provides better organization, scalability, and maintainability in the long run, 
making the system more manageable and understandable for both ends of the user and programmer. In terms of numbers, 
it will take 7 baseline smart contracts that always need to be featured, with the rest of them depending of the number 
of assets and their categories. Here is an example of how that may look schematically, and then how it would look with inputs and outputs:
1. User Management Contract
    - Manages user registration, authentication, and access control to the platform.

2. Inheritance Plan Management Contract
    - Handles the creation, modification, and deletion of inheritance plans.
    - Contains functions related to specifying assets, beneficiaries, and conditions.

3. Asset Management Contracts:
    - Real Estate Contract: Manages real estate assets and their transfers.
    - Financial Assets Contract:Handles stocks, bonds, and other financial instruments.
    - Artwork Contract: Manages artwork and collectibles.
    - Business Interests Contract: Deals with ownership stakes in businesses.
    - Insurance Policies Contract: Manages insurance policies and their beneficiaries.
    - Debts and Loans Contract: Handles loans, debts, and their transfers.

4. Identity Verification Contract:
    -  Verifies the identity of contract parties such as beneficiaries and legal representatives.

5. Transaction Record Contract:
    - Records all transactions and changes made to the inheritance plans, providing transparency and auditability.

6. Confirm Passing Function:
    - Confirms the passing of the participant, enabling the execution of the estate 
plan.
 
7. Execute Estate Function:
    - Executes the inheritance plan, transferring funds and assets to the designated 
beneficiaries as per the established plan.

8.  Contract Initialization
    - Initializes the contract with the address of the deceased participant and sets the  
executor as the deployer of the contract.

There are some modifiers to consider as well, such as the Only Executor Modifier and Only After Death Confirmation Modifier. These restrict certain functions to be accessible only by the executor (the entity responsible for executing the estate plan) and ensures that specific functions can only be called after the death of the participant has been confirmed, respectively. Here is how it would look from an input/output perspective:
1. User Management Contract:
- Register User Function:
  - Inputs:
	- None. The function captures `msg.sender` automatically when called.
  - Expected Behavior/Role:
	- Registers the user within the system.
  - Outputs:
	- None.
- Authenticate User Function:
  - Inputs:
	- None. The function uses `msg.sender` for authentication.
  - Expected Behavior/Role:
	- Verifies if the sender is a registered user.
  - Outputs:
	- `isAuthenticated`: Boolean indicating whether the sender is authenticated.
2. Inheritance Plan Management Contract:
- Create Inheritance Plan Function:
  - Inputs:
	- `userAddress`: Address of the user creating the plan.
	- `assetDetails`: Details of the assets to be distributed.
	- `beneficiaryDetails`: Details of the beneficiaries.
	- `conditions`: Triggers and conditions for asset distribution.
  - Expected Behavior/Role:
	- Captures `userAddress` automatically from the transaction.
	- Creates a customized inheritance plan based on the provided inputs.
  - Outputs:
	- `planID`: Unique identifier for the created inheritance plan.

- Modify Inheritance Plan Function:
  - Inputs:
	- `planID`: Identifier of the plan to be modified.
	- `updatedDetails`: Updated information for the plan.
 - Expected Behavior/Role:
	- Captures `msg.sender` automatically, verifying the executor.
	- Allows users to modify existing inheritance plans.
  - Outputs:
	- `success`: Boolean indicating whether the modification was successful.

3. Asset Management Contracts:
- Real Estate Contract:
  - Inputs:
	- `ownerAddress`: Address of the asset owner adding the real estate asset to the system.
	- `assetDetails`: Details of the real estate property.
  - Expected Behavior/Role:
	- Captures `msg.sender` automatically.
	- Creates a new real estate asset entry in the system.
  - Outputs:
	- `assetID`: Unique identifier for the created real estate asset.

- Financial Assets Contract:
  - Inputs:
	- `ownerAddress`: Address of the owner adding the financial asset.
	- `assetDetails`: Details of the financial instrument.
  - Expected Behavior/Role:
	- Captures `msg.sender` automatically.
	- Adds the financial asset to the owner's portfolio.
  - Outputs:
	- `assetID`: Unique identifier for the created financial asset.

- Artwork Contract:
  - Inputs:
	- `ownerAddress`: Address of the artwork owner.
	- `artworkDetails`: Details of the artwork, such as artist, medium, etc.
  - Expected Behavior/Role:
	- Captures `msg.sender` automatically.
	- Registers the artwork under the owner's name.
  - Outputs:
	- `artworkID`: Unique identifier for the registered artwork.

(Similar input, behavior, and outputs can be defined for Business Interests Contract, Insurance Policies Contract, and Debts and Loans Contract.)

4. Identity Verification Contract:
- Verify Identity Function:
  - Inputs:
	- `userAddress`: Address of the user to be verified.
	- `verificationDocuments`: Documents for identity verification.
  - Expected Behavior/Role:
	- Captures `msg.sender` automatically.
	- Verifies the identity of the user based on the provided documents.
  - Outputs:
	- `isVerified`: Boolean indicating whether the user is verified.
5. Transaction Record Contract:
- Record Transaction Function:
  - Inputs:
	- `userAddress`: Address of the user initiating the transaction.
	- `transactionDetails`: Details of the transaction or change made.
  - Expected Behavior/Role:
	- Captures `msg.sender` automatically.
	- Records the transaction or change for auditing purposes.
  - Outputs:
	- `transactionID`: Unique identifier for the recorded transaction.

Modifiers:
- Only Executor Modifier:
  - Description: Restricts certain functions to be accessible only by the executor, ensuring that critical actions are executed by authorized entities responsible for estate management.

- Only After Death Confirmation Modifier:
  - Description: Ensures that specific functions can only be called after the death of the participant has been confirmed, providing an additional layer of security and authenticity to the estate execution process.
## Example of Smart Contract Code""")

imagec = Image.open('code.jpg')
st.image(imagec,caption="Asset Management Demo Contract", width=700)

st.markdown("## Theoretical Process from Consumer Perspective")

st.divider()
st.markdown("Upon registering on the estate planning app, users embark on a streamlined onboarding process, establishing a secure account and completing their profiles with essential personal and financial information. The platform prioritizes user education, offering interactive tutorials and informative content to elucidate the significance of estate planning, dispelling common misconceptions, and outlining the benefits of a well-crafted plan.

As users delve into the planning phase, the app provides a user-friendly interface for creating a comprehensive digital inventory of assets, ranging from financial holdings to real estate and personal belongings. The intuitive design ensures that users can easily designate beneficiaries for each asset, promoting clarity and transparency in the wealth transfer process. Should users encounter more complex legal considerations, the app seamlessly integrates legal guidance or access to professionals to ensure their plans align with current legal frameworks.

Moving forward, the app guides users through the creation of their wills with an intuitive interface, offering prompts and suggestions to cover essential aspects of the document. Notably, the integration of smart contracts becomes a cornerstone of the process. When users finalize their wills, the app compiles these legal instructions into a smart contract, a self-executing digital agreement powered by blockchain technology. This compilation ensures that the terms and conditions outlined in the will are translated into a secure and immutable digital format.

In the event of a user's passing, the smart contract is automatically triggered, initiating the seamless execution of the specified instructions. This process is designed to be swift, efficient, and transparent, minimizing the complexities often associated with traditional probate proceedings. The smart contract facilitates the automated transfer of assets to designated beneficiaries, ensuring that the user's wishes are faithfully and precisely carried out.

The use of blockchain technology in compiling and executing smart contracts provides an additional layer of security. Each transaction and action related to the estate plan is recorded on the blockchain, creating a permanent and unalterable record. This not only enhances transparency but also guards against potential disputes or fraudulent activities, providing both the testator and beneficiaries with confidence in the integrity of the estate planning process.

Throughout this user experience journey, the app remains committed to demystifying estate planning and promoting awareness. Its inclusive design addresses disparities in adoption, offering educational initiatives that empower individuals from diverse backgrounds. By making estate planning accessible, efficient, and comprehensible, the app strives to contribute to the overall resilience, prosperity, and financial well-being of families and communities.")
