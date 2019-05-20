module.exports = {
  env: {
    es6: true,
    node: true
  },
  extends: ["standard"],
  plugins: ["@typescript-eslint/eslint-plugin"],
  parser: "@typescript-eslint/parser",
  rules: {
    // TypeScript styling.
    "@typescript-eslint/no-explicit-any": ["error"],
    "@typescript-eslint/type-annotation-spacing": ["error"],
    "@typescript-eslint/no-namespace": ["error"],
    "@typescript-eslint/interface-name-prefix": ["error"],
    "@typescript-eslint/no-angle-bracket-type-assertion": ["error"],
    // Fix no-unused-vars.
    "@typescript-eslint/no-unused-vars": ["error"]
  }
}
