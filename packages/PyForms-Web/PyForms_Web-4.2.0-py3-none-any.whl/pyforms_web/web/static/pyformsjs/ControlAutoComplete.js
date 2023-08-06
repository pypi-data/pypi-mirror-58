class ControlAutoComplete extends ControlBase{

    

    init_control(){
        var html = "<div id='"+this.place_id()+"' class='field control ControlAutoComplete' ><label>"+this.properties.label+"</label>";
        html += "<div class='ui search dropdown "+(this.properties.multiple?'multiple':'')+" selection' id='"+this.control_id()+"' >"
        html += '<i class="ui search small icon"></i>';
        html += '<div class="default text">'+this.properties.label+'</div>';
        html += '</div>';
        this.jquery_place().replaceWith(html);

        // get the items from an url
        this.jquery().dropdown({
            apiSettings: { url: this.properties.items_url, cache:false },
            saveRemoteData:   false,
            placeholder: false,
            forceSelection: false
        });

        this.jquery().dropdown('setup menu', { values: this.properties.items });
        this.set_value(this.properties.value);

        var self = this;
        this.jquery().dropdown('setting', 'onChange', function(){
            if(self.flag_exec_on_change_event)
                self.basewidget.fire_event( self.name, 'update_control_event' );
        });

        if(this.properties.error)    this.jquery_place().addClass('error'); else this.jquery_place().removeClass('error');
		if(this.properties.required) this.set_required();
    };

    ////////////////////////////////////////////////////////////////////////////////

    set_value(value){
        this.flag_exec_on_change_event = false;
        if(!this.properties.multiple) value = [value]
        this.jquery().dropdown('set exactly', value);
        this.flag_exec_on_change_event = true;

    };

    ////////////////////////////////////////////////////////////////////////////////

    get_value(){
        var v = this.jquery().dropdown('get value')
        if(this.properties.multiple){
            if( v.length==0 ) return [];
            return v==''?[]:v.split(',')  
        }else{
            if( v.length==0 ) return null;
            return v==''?null:v
        }
    };

    ////////////////////////////////////////////////////////////////////////////////

    deserialize(data){
        this.properties = $.extend(this.properties, data);
        this.jquery().dropdown('setup menu', { values: this.properties.items });
        this.set_value(this.properties.value);


        if(this.properties.error) this.jquery_place().addClass('error'); else this.jquery_place().removeClass('error'); 
    };

    ////////////////////////////////////////////////////////////////////////////////


    update_server(){
        var current = this.properties.value;
        var newval  = this.get_value();

        if(!this.properties.multiple)
            return newval!=current;
        else{
            current.sort();
            newval.sort();

            if(newval.length!=current.length) return true;

            for(var i=0; i<newval.length; i++){
                if( newval[i]!=(current[i]+'') ) return true;
            }

            return false;
        }
    }
}
