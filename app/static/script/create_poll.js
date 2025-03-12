let number_fields = 0

    function append_field() {
        number_fields+=1
        let tbody = document.createElement("tbody");
        tbody.className = "field-tbody"
        let tbody_answers = document.createElement("tbody");
        tbody_answers.className = "field-tbody field-tbody-answers"
        tbody_answers.id = `answers-fields-${number_fields-1}-field_type`

        tbody.innerHTML = `` +
            `<tr><td colspan="2"><hr></td></tr><tr>` +
            `<td><label for="fields-${number_fields-1}-field_name">Name</label></td>` +
            `<td><input id="fields-${number_fields-1}-field_name" name="fields-${number_fields-1}-field_name" required="" type="text"></td></tr>` +

            `<tr><td><label for="fields-${number_fields-1}-field_type">Field Type</label></td>` +
            `<td><select id="fields-${number_fields-1}-field_type" name="fields-${number_fields-1}-field_type" required="">` +
            `<option value="100">Single Choice</option><option value="101">Multi Choice</option>` +
            `<option value="102">Ranking</option><option value="200">Open Text</option></select>` +
            `</td></tr>`;
        tbody_answers.innerHTML = `` +
            `<tr><td><label for="fields-${number_fields-1}-anwser_possibilities">Choices</label></td>` +
            `             <td><input id="fields-${number_fields-1}-anwser_possibilities-0" name="fields-${number_fields-1}-answer_possibilities-0" type="text"></td></tr>` +
            `<tr><td></td><td><input id="fields-${number_fields-1}-answer_possibilities-1" name="fields-${number_fields-1}-answer_possibilities-1" type="text"></td></tr>` +
            `<tr><td></td><td><input id="fields-${number_fields-1}-answer_possibilities-2" name="fields-${number_fields-1}-answer_possibilities-2" type="text"></td></tr>` +
            `<tr><td></td><td><input id="fields-${number_fields-1}-answer_possibilities-3" name="fields-${number_fields-1}-answer_possibilities-3" type="text"></td></tr>` +
            `<tr><td></td><td><input id="fields-${number_fields-1}-answer_possibilities-4" name="fields-${number_fields-1}-answer_possibilities-4" type="text"></td></tr>`;

        document.getElementById("fields-table").appendChild(tbody);
        document.getElementById("fields-table").appendChild(tbody_answers);

        let selector = document.getElementById(`fields-${number_fields-1}-field_type`);
        selector.addEventListener("change", function () {
            document.getElementById(`answers-fields-${number_fields-1}-field_type`).hidden = Math.floor(selector.value / 100) !== 1;
        })
    }
    function reset_fields() {
        if (!confirm("RESET?")) return

        document.querySelectorAll('table .field-tbody').forEach(tbody => tbody.remove());
        number_fields = 0
        append_field()
    }