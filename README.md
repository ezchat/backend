# ez.chat backend

[![Requirements](https://img.shields.io/badge/requires-Node.js%208+-brightgreen.svg?style=popout&logo=node.js)](https://nodejs.org/download)

The backend for ez.chat, built with Polka and TypeScript.

## Setup

This assumes you have Node.js 8+ in PATH as `node`, and Yarn installed and available as `yarn`. If using `npm`, follow commands in brackets. Yarn is preferable to use over npm for this project.

To install required dependencies, run `yarn` (`npm install`) to install the dependencies in `node_modules`.

This project utilizes TypeScript. To startup the server in development mode, run `yarn dev` (`npm run dev`) which will cache TypeScript builds, allow live code reload and get detailed errors.

To run the server in production mode, run `yarn build` (`npm run build`) to build TypeScript in `src/` and output to `dist/` followed by `yarn start` which will run `node dist/index.js` i.e. transpiled TypeScript.

To lint the project, run `yarn lint` to lint the server and `yarn mongo` to startup a test database (make a folder `database/` for the first time)
