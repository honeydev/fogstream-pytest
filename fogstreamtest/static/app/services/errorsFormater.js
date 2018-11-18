'use strict';

class ErrorsFormater {

    constructor() {
        this.EXCEPTIONS = ['non_field_errors'];
    }

    format(errors) {
        let formatedErrors = [];
        for (let errorType in errors) {
            if (this.EXCEPTIONS.includes(errorType)) {
                formatedErrors = formatedErrors.concat(errors[errorType]);
                continue;
            }
            formatedErrors = formatedErrors.concat(this.joinErrorTypeAndErrorMessage(errorType, errors[errorType]));
        }
        return formatedErrors;
    }

    joinErrorTypeAndErrorMessage(errorType, messages) {
        return messages.map((message) => {
            return `${this.ucfirst(errorType)} ${message}`;
        })
    }

    ucfirst(string) {
         return string.charAt(0).toUpperCase() + string.slice(1);
    }
}

export default ErrorsFormater;