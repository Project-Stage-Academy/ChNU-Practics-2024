# Forum-Project-Stage-CC
Forum Project Stage CC Template Repo

**Project Vision Statement:**

*"Empowering Innovation: Bridging Startups and Investors for Ukraine's Economic Growth"*

**Overview:**

In the dynamic world of entrepreneurship, the path from a transformative idea to a successful venture is often complex and challenging. Our WebAPI application, developed using the Django Rest Framework, is designed to be a cornerstone in simplifying this journey. We aim to create a robust and secure digital platform that caters to two pivotal groups in the business ecosystem: innovative startups with compelling ideas and forward-thinking investors seeking valuable opportunities.

**Goals:**

1. **Fostering Collaborative Opportunities:** Our platform bridges startups and investors, enabling startups to showcase their groundbreaking proposals and investors to discover and engage with high-potential ventures.

2. **Seamless User Experience:** We prioritize intuitive navigation and interaction, ensuring that startups and investors can easily connect, communicate, and collaborate.

3. **Secure and Trustworthy Environment:** Security is at the forefront of our development, ensuring the confidentiality and integrity of all shared information and communications.

4. **Supporting Economic Growth:** By aligning startups with the right investors, our platform not only cultivates individual business success but also contributes significantly to the growth and diversification of Ukraine's economy.

**Commitment:**

We are committed to delivering a platform that is not just a marketplace for ideas and investments but a thriving community that nurtures innovation fosters economic development, and supports the aspirations of entrepreneurs and investors alike. Our vision is to see a world where every transformative idea has the opportunity to flourish and where investors can confidently fuel the engines of progress and innovation.

![image](https://github.com/mehalyna/Forum-Project-Stage-CC/assets/39273210/54b0de76-f6e3-4bf3-bf38-fb5bf1d1d63d)



### Basic Epics

0. **As a user of the platform**, I want the ability to represent both as a startup and as an investor company, so that I can engage in the platform's ecosystem from both perspectives using a single account.

   - Features:
     - implement the functionality for users to select and switch roles.

2. **As a startup company,** I want to create a profile on the platform, so that I can present my ideas and proposals to potential investors.
   
   - Features:
     -  user registration functionality for startups.
     -  profile setup page where startups can add details about their company and ideas.

3. **As an investor,** I want to view profiles of startups, so that I can find promising ideas to invest in.
   
   - Features:
     -  feature for investors to browse and filter startup profiles.
     -  viewing functionality for detailed startup profiles.

4. **As a startup company,** I want to update my project information, so that I can keep potential investors informed about our progress and milestones.
   
   - Features:
     -  functionality for startups to edit and update their project information.
     -  system to notify investors about updates to startups they are following.

5. **As an investor,** I want to be able to contact startups directly through the platform, so that I can discuss investment opportunities.
   
   - Features:
     -  secure messaging system within the platform for communication between startups and investors.
     -  privacy and security measures to protect the communication.

6. **As a startup company,** I want to receive notifications about interested investors, so that I can engage with them promptly.
   
   - Features:
     -  notification functionality for startups when an investor shows interest or contacts them.
     -  dashboard for startups to view and manage investor interactions.

7. **As an investor,** I want to save and track startups that interest me, so that I can manage my investment opportunities effectively.
   
   - Features:
     -  feature for investors to save and track startups.
     -  dashboard for investors to manage their saved startups and investment activities.

### Additional Features

- **Security and Data Protection**: Ensure that user data, especially sensitive financial information, is securely handled.
  
- **User Feedback System**: Create a system for users to provide feedback on the platform, contributing to continuous improvement.

- **Analytical Tools**: Implement analytical tools for startups to understand investor engagement and for investors to analyze startup potential.

### Agile Considerations

- Each user story can be broken down into smaller tasks and developed in sprints.
- Regular feedback from both user groups (startups and investors) should be incorporated.

### Development setup

This weill ensure your Django project is ready to be used and developed locally.

As a first step, you'll need to clone the repository to your local machine:

```bash
$ git clone git@github.com:Project-Stage-Academy/ChNU-Practics-2024.git
```
After you've cloned the repository, you'll need to create and activate a git-ignored virtual env (venv or .venv), e.g.:

```bash
$ python -m venv .venv
$ source .venv/bin/activate # or .venv\Scripts\activate on Windows
```

Then, you'll need to install the dependencies, we using pyproject.toml for this:

```bash
$ pip install pip --upgrade
$ pip install -e .[development] # Install dev dependencies
```

Next step is creating .env file in root directory to properly docker create db

```bash
$ cp .env.example .env # or copy .env.example .env on Windows
```

Make sure you create `.env` and fill it the following variables:

```env
SECRET_KEY=mysecretdummy # Django Secret Key

POSTGRES_DB=mydb # Postgres Database Name
POSTGRES_USER=myuser # Postgres User
POSTGRES_PASSWORD=mysecretpassword # Postgres Password
POSTGRES_HOST=postgres # Postgres host, if you run server not in docker, it can be change to localhost
POSTGRES_PORT=5432 # Postgres port
```

Once you have the above `.env` file, run the following command to build and run container:

```bash
$ docker compose up --build # Add flag -d to run in background
```

This will create a postgresql database and djangos those are running in the background. To bring this down just run:

```bash
# or Ctrl+C if you are not running command in backround
$ docker compose down
```

> To run only database use this: `docker compose up postgres -d` and change in `.env` `POSTGRES_HOST` to `localhost`

**Applying migrations:**

```bash
$ docker compose exec -it app /opt/venv/bin/python src/manage.py makemigrations --noinput

$ docker compose exec -it app /opt/venv/bin/python src/manage.py migrate --noinput
```

### Contributing

**Install pre-commit**

```bash
$ pre-commit install # run it in virtualenv
```

**Create a New Branch**

Before making any changes, it's a good practice to create a new branch for your feature or fix. This keeps your changes isolated and makes it easier to manage and review.

```bash
$ git checkout develop
$ git checkout -b {id-issue}-new-feature-name # replace {id-issue} with id of issue, e.x. 4-JWT_Authentication, 25-setup-docker
```
**Make Changes and Test**

Make the necessary changes to implement your new feature or fix the issue. Ensure that your changes do not break existing functionality, and test thoroughly.

**Commit Changes**

Once you are satisfied with your changes, commit them with a clear and concise commit message.

```bash
$ git add .
$ git commit -m "Implementing new feature or fixing issue"
```

**Push Changes to Repository**

```bash
$ git push -u origin {id-issue}-new-feature-name # replace {id-issue} with id of issue, e.x. 4-JWT_Authentication, 25-setup-docker
```

**Create a Pull Request**

Go to the GitHub repository, and you should see a prompt to create a new pull request. Click on it, and GitHub will guide you through the process of creating a pull request. Select the branch you just pushed, provide a descriptive title and comment, and create the pull request. 

Or using [github cli](https://cli.github.com/):

```bash
$ gh pr create --base develop
```

**Merge Pull Request**

Once your pull request has been approved and passes all checks, you can merge it into the develop branch.

**Cleanup**

After merging, you can delete the feature branch locally.

```bash
$ git checkout develop
$ git branch -d {id-issue}-new-feature-name # replace {id-issue} with id of issue, e.x. 4-JWT_Authentication, 25-setup-docker
```
